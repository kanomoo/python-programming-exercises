# def divide_plot(x: int, y: int, z: int, start: str) -> str:
#     T = (x + y + z) // 3
    
#     def get_ab_ops(pos):
#         diff, ops = T - x, []
#         if diff > 0:
#             if pos == 'B': ops.append('LEFT')
#             elif pos == 'C': ops.extend(['LEFT', 'LEFT'])
#             pos = 'A'
#             ops.append(f'PUSH_RIGHT {diff}')
#         elif diff < 0:
#             if pos == 'A': ops.append('RIGHT')
#             elif pos == 'C': ops.append('LEFT')
#             pos = 'B'
#             ops.append(f'PUSH_LEFT {-diff}')
#         return ops, pos

#     def get_bc_ops(pos):
#         diff, ops = T - z, []
#         if diff > 0:
#             if pos == 'A': ops.extend(['RIGHT', 'RIGHT'])
#             elif pos == 'B': ops.append('RIGHT')
#             pos = 'C'
#             ops.append(f'PUSH_LEFT {diff}')
#         elif diff < 0:
#             if pos == 'A': ops.append('RIGHT')
#             elif pos == 'C': ops.append('LEFT')
#             pos = 'B'
#             ops.append(f'PUSH_RIGHT {-diff}')
#         return ops, pos

#     gain_B_from_1 = x - T
#     gain_B_from_2 = z - T

#     ops_sequence = []
#     pos = start

#     if gain_B_from_1 < 0 and gain_B_from_2 > 0:
#         ops, pos = get_bc_ops(pos)
#         ops_sequence.extend(ops)
#         ops, pos = get_ab_ops(pos)
#         ops_sequence.extend(ops)
#     else:
#         ops, pos = get_ab_ops(pos)
#         ops_sequence.extend(ops)
#         ops, pos = get_bc_ops(pos)
#         ops_sequence.extend(ops)

#     return(', '.join(ops_sequence))

# def simulate_operations(x: int, y: int, z: int, start: str, ops_str: str) -> str:
#     if not ops_str: return f"{x} {y} {z}"
        
#     ops = ops_str.split(', ')
#     pos = start
    
#     for op in ops:
#         if op == 'LEFT':
#             if pos == 'B': pos = 'A'
#             elif pos == 'C': pos = 'B'
#             else: return "ภารกิจล้มเหลว"
#         elif op == 'RIGHT':
#             if pos == 'A': pos = 'B'
#             elif pos == 'B': pos = 'C'
#             else: return "ภารกิจล้มเหลว"
#         elif op.startswith('PUSH_LEFT'):
#             n = int(op.split()[1])
#             if pos == 'A': return "ภารกิจล้มเหลว"
#             elif pos == 'B': x -= n; y += n
#             elif pos == 'C': y -= n; z += n
#         elif op.startswith('PUSH_RIGHT'):
#             n = int(op.split()[1])
#             if pos == 'A': x += n; y -= n
#             elif pos == 'B': y += n; z -= n
#             elif pos == 'C': return "ภารกิจล้มเหลว"
            
#         if x < 1 or y < 1 or z < 1:
#             return "ภารกิจล้มเหลว"
            
#     return f"{x} {y} {z}"

# if __name__ == "__main__":
#     print(divide_plot(2, 5, 8, "A"))           # RIGHT, PUSH_RIGHT 3, LEFT, PUSH_RIGHT 3
#     print(divide_plot(2, 5, 8, "B"))           # PUSH_RIGHT 3, RIGHT, PUSH_RIGHT 3
#     print(divide_plot(60, 60, 60, "B"))        # None
    
#     ops = divide_plot(2, 5, 8, "A")
#     print(simulate_operations(2, 5, 10, "A", ops))  # 5 5 5


