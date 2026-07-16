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
#     print(divide_plot(2, 5, 8, "A"))           # PUSH_RIGHT 3, RIGHT, PUSH_RIGHT 3
#     print(divide_plot(60, 60, 60, "B"))        # None
    
#     ops = divide_plot(2, 5, 8, "A")
#     print(simulate_operations(2, 5, 10, "A", ops))  # 5 5 5






# def concat_ops(op1: str, op2: str) -> str:
#     # ต่อข้อความคำสั่งสองชุดเข้าด้วยกันโดยเว้นด้วยเครื่องหมายคอมมาและเว้นวรรค
#     if not op1 and not op2: return ""
#     if not op1: return op2
#     if not op2: return op1
#     return op1 + ", " + op2


# def get_moves(curr: str, target: str) -> str:
#     # ฟังก์ชันย่อยสำหรับสร้างคำสั่งเดินจากจุดปัจจุบัน (curr) ไปยังเป้าหมาย (target)
#     if curr == 'A':
#         if target == 'B': return 'RIGHT'
#         if target == 'C': return 'RIGHT, RIGHT'
#     elif curr == 'B':
#         if target == 'A': return 'LEFT'
#         if target == 'C': return 'RIGHT'
#     elif curr == 'C':
#         if target == 'A': return 'LEFT, LEFT'
#         if target == 'B': return 'LEFT'
#     return ""

# def divide_plot(x: int, y: int, z: int, start: str) -> str:
#     T = (x + y + z) // 3
    
#     L1_diff = T - x
#     L1_plot = ""
#     L1_action = ""
#     if L1_diff > 0:
#         L1_plot = 'A'
#         L1_action = 'PUSH_RIGHT ' + str(L1_diff)
#     elif L1_diff < 0:
#         L1_plot = 'B'
#         L1_action = 'PUSH_LEFT ' + str(-L1_diff)
        
#     L2_diff = (2 * T) - (x + y)
#     L2_plot = ""
#     L2_action = ""
#     if L2_diff > 0:
#         L2_plot = 'B'
#         L2_action = 'PUSH_RIGHT ' + str(L2_diff)
#     elif L2_diff < 0:
#         L2_plot = 'C'
#         L2_action = 'PUSH_LEFT ' + str(-L2_diff)
        
#     ops = ""
#     curr = start
    
#     if (2 * T) - x >= 1:
#         if L2_plot != "":
#             ops = concat_ops(ops, get_moves(curr, L2_plot))
#             ops = concat_ops(ops, L2_action)
#             curr = L2_plot
#         if L1_plot != "":
#             ops = concat_ops(ops, get_moves(curr, L1_plot))
#             ops = concat_ops(ops, L1_action)
#             curr = L1_plot
#     else:
#         if L1_plot != "":
#             ops = concat_ops(ops, get_moves(curr, L1_plot))
#             ops = concat_ops(ops, L1_action)
#             curr = L1_plot
#         if L2_plot != "":
#             ops = concat_ops(ops, get_moves(curr, L2_plot))
#             ops = concat_ops(ops, L2_action)
#             curr = L2_plot
            
#     return ops

# if __name__ == '__main__':
#     from HW04_3_helper import simulate_operations
    
#     print(divide_plot(2, 5, 8, 'A'))
    
#     print(divide_plot(2, 5, 8, 'A'))
    
#     print(divide_plot(60, 60, 60, 'B'))
    
#     ops = divide_plot(2, 5, 8, 'A')
#     result = simulate_operations(2, 5, 8, 'A', ops)
#     print(result)




# def concat_ops(op1: str, op2: str) -> str:
#     if not op1 and not op2:
#         return ''
#     if not op1:
#         return op2
#     if not op2:
#         return op1
#     return op1 + ', ' + op2

# def get_moves(curr: str, target: str) -> str:
#     if curr == 'A':
#         if target == 'B': return 'RIGHT'
#         if target == 'C': return 'RIGHT, RIGHT'
#     elif curr == 'B':
#         if target == 'A': return 'LEFT'
#         if target == 'C': return 'RIGHT'
#     elif curr == 'C':
#         if target == 'A': return 'LEFT, LEFT'
#         if target == 'B': return 'LEFT'
#     return ""

# def divide_plot(x: int, y: int, z: int, start: str) -> str:
#     ops = ''
#     T = (x + y + z) // 3
    
#     L1_diff = T - x
#     L1_plot = ""
#     L1_action = ""
#     if L1_diff > 0:
#         L1_plot = 'A'
#         L1_action = 'PUSH_RIGHT ' + str(L1_diff)
#     elif L1_diff < 0:
#         L1_plot = 'B'
#         L1_action = 'PUSH_LEFT ' + str(-L1_diff)
        
#     L2_diff = (2 * T) - (x + y)
#     L2_plot = ""
#     L2_action = ""
#     if L2_diff > 0:
#         L2_plot = 'B'
#         L2_action = 'PUSH_RIGHT ' + str(L2_diff)
#     elif L2_diff < 0:
#         L2_plot = 'C'
#         L2_action = 'PUSH_LEFT ' + str(-L2_diff)
        
#     curr = start
    
#     can_L1_first = ((x + y) - T) >= 1
#     can_L2_first = ((2 * T) - x) >= 1
    
#     do_L1_first = True
#     if can_L1_first and can_L2_first:
#         if start == 'C':
#             do_L1_first = False
#     elif not can_L1_first:
#         do_L1_first = False
        
#     if do_L1_first:
#         if L1_plot != "":
#             ops = concat_ops(ops, get_moves(curr, L1_plot))
#             ops = concat_ops(ops, L1_action)
#             curr = L1_plot
#         if L2_plot != "":
#             ops = concat_ops(ops, get_moves(curr, L2_plot))
#             ops = concat_ops(ops, L2_action)
#             curr = L2_plot
#     else:
#         if L2_plot != "":
#             ops = concat_ops(ops, get_moves(curr, L2_plot))
#             ops = concat_ops(ops, L2_action)
#             curr = L2_plot
#         if L1_plot != "":
#             ops = concat_ops(ops, get_moves(curr, L1_plot))
#             ops = concat_ops(ops, L1_action)
#             curr = L1_plot
            
#     # ไม่แก้บรรทัดนี้
#     return ops.strip(', ')

# if __name__ == '__main__':
#     from HW04_3_helper import simulate_operations
#     ops = divide_plot(2, 5, 8, 'A')
    
#     print("Operations:", ops)
    
#     result = simulate_operations(2, 5, 8, 'A', ops)
#     print(result)





# def divide_plot(x: int, y: int, z: int, start: str) -> str:
#     ops = ''

#     T = (x + y + z) // 3
    
#     L1_diff = T - x
#     L1_plot = ""
#     L1_act = ""
#     if L1_diff > 0:
#         L1_plot = 'A'
#         L1_act = 'PUSH_RIGHT ' + str(L1_diff)
#     elif L1_diff < 0:
#         L1_plot = 'B'
#         L1_act = 'PUSH_LEFT ' + str(-L1_diff)
        
#     L2_diff = (2 * T) - (x + y)
#     L2_plot = ""
#     L2_act = ""
#     if L2_diff > 0:
#         L2_plot = 'B'
#         L2_act = 'PUSH_RIGHT ' + str(L2_diff)
#     elif L2_diff < 0:
#         L2_plot = 'C'
#         L2_act = 'PUSH_LEFT ' + str(-L2_diff)
        
#     can_L2_first = ((2 * T) - x) >= 1
#     can_L1_first = ((x + y) - T) >= 1
    
#     do_L2_first = can_L2_first
#     if not can_L2_first:
#         do_L2_first = False
#     if not can_L1_first:
#         do_L2_first = True
        
#     if do_L2_first:
#         move1 = get_moves(start, L2_plot)
#         curr_after_L2 = L2_plot if L2_plot != "" else start
#         move2 = get_moves(curr_after_L2, L1_plot)
        
#         part1 = concat_ops(move1, L2_act)
#         part2 = concat_ops(move2, L1_act)
#         ops = concat_ops(part1, part2)
#     else:
#         move1 = get_moves(start, L1_plot)
#         curr_after_L1 = L1_plot if L1_plot != "" else start
#         move2 = get_moves(curr_after_L1, L2_plot)
        
#         part1 = concat_ops(move1, L1_act)
#         part2 = concat_ops(move2, L2_act)
#         ops = concat_ops(part1, part2)

#     return ops.strip(', ')

# def concat_ops(op1: str, op2: str) -> str:
#     if not op1 and not op2:
#         return ''
#     if not op1:
#         return op2
#     if not op2:
#         return op1
        
#     return ', '.join([op1, op2])

# def get_moves(curr: str, target: str) -> str:
#     if not curr or not target or curr == target:
#         return ""
#     if curr == 'A':
#         if target == 'B': return 'RIGHT'
#         if target == 'C': return 'RIGHT, RIGHT'
#     elif curr == 'B':
#         if target == 'A': return 'LEFT'
#         if target == 'C': return 'RIGHT'
#     elif curr == 'C':
#         if target == 'A': return 'LEFT, LEFT'
#         if target == 'B': return 'LEFT'
#     return ""

# if __name__ == '__main__':
#     from HW04_3_helper import simulate_operations
#     ops = divide_plot(2, 5, 8, 'A')
#     result = simulate_operations(2, 5, 8, 'A', ops)
#     print(result)



# def divide_plot(x: int, y: int, z: int, start: str) -> str:
#     T = (x + y + z) // 3
#     d1, d2 = T - x, (2 * T) - (x + y)
    
#     p1 = 'A' if d1 > 0 else ('B' if d1 < 0 else "")
#     a1 = 'PUSH_RIGHT ' + str(d1) if d1 > 0 else ('PUSH_LEFT ' + str(-d1) if d1 < 0 else "")
    
#     p2 = 'B' if d2 > 0 else ('C' if d2 < 0 else "")
#     a2 = 'PUSH_RIGHT ' + str(d2) if d2 > 0 else ('PUSH_LEFT ' + str(-d2) if d2 < 0 else "")
    
#     if ((2 * T) - x) >= 1 or ((x + y) - T) < 1:
#         m1 = get_moves(start, p2)
#         m2 = get_moves(p2 or start, p1) # ถ้า p2 เป็นค่าว่าง ให้ใช้ start แทน
#         ops = concat_ops(concat_ops(m1, a2), concat_ops(m2, a1))
#     else:
#         m1 = get_moves(start, p1)
#         m2 = get_moves(p1 or start, p2)
#         ops = concat_ops(concat_ops(m1, a1), concat_ops(m2, a2))

#     return ops.strip(', ')

# def concat_ops(op1: str, op2: str) -> str:
#     if not op1 and not op2: return ''
#     if not op1: return op2
#     if not op2: return op1
#     return ', '.join([op1, op2])

# def get_moves(c: str, t: str) -> str:
#     if not c or not t or c == t: return ""
#     if c == 'A': return 'RIGHT' if t == 'B' else 'RIGHT, RIGHT'
#     if c == 'B': return 'LEFT' if t == 'A' else 'RIGHT'
#     return 'LEFT' if t == 'B' else 'LEFT, LEFT'

# if __name__ == '__main__':
#     from HW04_3_helper import simulate_operations
#     ops = divide_plot(2, 5, 8, 'A')
#     result = simulate_operations(2, 5, 8, 'A', ops)
#     print(result)


def divide_plot(x: int, y: int, z: int, start: str) -> str:
    a, b, c = x, y, z
    if a == b and b == c: return ""
    ops, position = "", start
    target = (x + y + z) // 3
    diff_a, diff_b, diff_c = target - a, target - b, target - c
    if diff_a > 0:
        a -= diff_a
        b += diff_a
        diff_b += a
    


    return ops.strip(", ")

def left(position):
    if position == "A": return ""
    elif position == "B": return "A"
    elif position == "C": return "B"

def right(position):
    if position == "A": return "B"
    elif position == "B": return "C"
    elif position == "C": return ""


def concat_ops(op1: str, op2: str) -> str:
    if not op1 and not op2: return ""
    if not op1: return op2
    if not op2: return op1
    return ", ".join([op1, op2])

if __name__ == "__main__":
    from HW04_3_helper import simulate_operations
    print(divide_plot(2, 5, 8, "A"))
    print(divide_plot(60, 60, 60, "B"))