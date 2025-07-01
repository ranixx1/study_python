import heapq

SFL = 200
GFL = 100

nodes = []
edges_data = {}
adj_list = {}
constrained_transitions = {}

node_flow_counts = {}
group_flow_users = {}

successful_paths_output = []
total_successful_distance = 0
successful_flow_count = 0

NodeCount, EdgeCount, ConstrainedCount, FlowCount = map(int, input().split())

for _ in range(EdgeCount):
    eid, gid, s_node, e_node, dist, cap = map(int, input().split())
    edges_data[eid] = {
        'group_id': gid,
        'start_node': s_node,
        'end_node': e_node,
        'distance': dist,
        'capacity': cap,
        'current_capacity_usage': 0
    }
    adj_list.setdefault(s_node, []).append((e_node, eid))
    adj_list.setdefault(e_node, []).append((s_node, eid))

    node_flow_counts[s_node] = 0
    node_flow_counts[e_node] = 0
    group_flow_users.setdefault(s_node, {})
    group_flow_users.setdefault(e_node, {})
    group_flow_users[s_node].setdefault(gid, set())
    group_flow_users[e_node].setdefault(gid, set())


for _ in range(ConstrainedCount):
    node_id, edge1, edge2 = map(int, input().split())
    constrained_transitions.setdefault(node_id, set()).add(frozenset({edge1, edge2}))

flows_data = []
for _ in range(FlowCount):
    flow_id, src_node, tgt_node, rate = map(int, input().split())
    flows_data.append({'flow_id': flow_id, 'source': src_node, 'target': tgt_node, 'rate': rate})

flows_data.sort(key=lambda f: (f['rate'], f['flow_id']))

def find_path(flow_id, source, target, rate):
    pq = [(0, source, {source}, [], None)]

    min_costs = {(source, frozenset({source})): 0}
    
    parents = {}

    while pq:
        current_cost, u, visited_nodes, current_path_edges, incoming_edge_id = heapq.heappop(pq)

        if current_cost > min_costs.get((u, frozenset(visited_nodes)), float('inf')):
            continue

        if u == target:
            return current_path_edges, current_cost

        for v, edge_id in adj_list.get(u, []):
            edge = edges_data[edge_id]

            if edge['current_capacity_usage'] + rate > edge['capacity']:
                continue

            if v in visited_nodes:
                continue

            if incoming_edge_id is not None and u in constrained_transitions:
                if frozenset({incoming_edge_id, edge_id}) in constrained_transitions[u]:
                    continue

            group_u_users = group_flow_users.get(u, {}).get(edge['group_id'], set())
            if u != source and len(group_u_users) >= GFL and flow_id not in group_u_users:
                 continue

            group_v_users = group_flow_users.get(v, {}).get(edge['group_id'], set())
            if v != target and len(group_v_users) >= GFL and flow_id not in group_v_users:
                 continue

            new_cost = current_cost + edge['distance']
            new_visited_nodes = visited_nodes.union({v})
            new_path_edges = current_path_edges + [edge_id]

            if new_cost < min_costs.get((v, frozenset(new_visited_nodes)), float('inf')):
                min_costs[(v, frozenset(new_visited_nodes))] = new_cost
                parents[(v, frozenset(new_visited_nodes))] = (u, incoming_edge_id)
                heapq.heappush(pq, (new_cost, v, new_visited_nodes, new_path_edges, edge_id))

    return None, None

for flow in flows_data:
    path_edges, path_distance = find_path(flow['flow_id'], flow['source'], flow['target'], flow['rate'])

    if path_edges:
        successful_flow_count += 1
        total_successful_distance += path_distance
        successful_paths_output.append(f"{flow['flow_id']} {' '.join(map(str, path_edges))}")

        for edge_id in path_edges:
            edges_data[edge_id]['current_capacity_usage'] += flow['rate']

        visited_nodes_in_path = set()
        
        current_trace_node = flow['source']
        for edge_id in path_edges:
            edge = edges_data[edge_id]
            
            if edge['start_node'] == current_trace_node:
                next_node = edge['end_node']
            else:
                next_node = edge['start_node']
            
            group_flow_users[current_trace_node][edge['group_id']].add(flow['flow_id'])
            group_flow_users[next_node][edge['group_id']].add(flow['flow_id'])
            
            visited_nodes_in_path.add(current_trace_node)
            visited_nodes_in_path.add(next_node)
            current_trace_node = next_node

        for node_in_path in visited_nodes_in_path:
            node_flow_counts[node_in_path] += 1

print(successful_flow_count)
for path_str in successful_paths_output:
    print(path_str)