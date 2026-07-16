def simulate_operations(x: int, y: int, z: int, start: str, ops: str) -> str:
    """
    ฟังก์ชันจำลองพฤติกรรม (สร้างขึ้นมาจำลองจากที่ต้อง import HW04_3_helper)
    *** ฟังก์ชันตัวช่วยนี้ไม่ได้นำไปตรวจเงื่อนไขเรื่อง Loop ของโจทย์ครับ ***
    """
    L1 = x
    L2 = x + y
    total = x + y + z
    curr = start
    
    if not ops:
        return f"{L1} {L2 - L1} {total - L2}"
        
    op_list = [op.strip() for op in ops.split(',') if op.strip()]
    
    for op in op_list:
        parts = op.split()
        cmd = parts[0]
        
        if cmd == 'LEFT':
            if curr == 'B': curr = 'A'
            elif curr == 'C': curr = 'B'
            else: return "ภารกิจล้มเหลว"
        elif cmd == 'RIGHT':
            if curr == 'A': curr = 'B'
            elif curr == 'B': curr = 'C'
            else: return "ภารกิจล้มเหลว"
        elif cmd == 'PUSH_LEFT':
            if len(parts) < 2: return "ภารกิจล้มเหลว"
            n = int(parts[1])
            if curr == 'A': return "ภารกิจล้มเหลว"
            elif curr == 'B': L1 -= n
            elif curr == 'C': L2 -= n
        elif cmd == 'PUSH_RIGHT':
            if len(parts) < 2: return "ภารกิจล้มเหลว"
            n = int(parts[1])
            if curr == 'A': L1 += n
            elif curr == 'B': L2 += n
            elif curr == 'C': return "ภารกิจล้มเหลว"
            
        wA = L1
        wB = L2 - L1
        wC = total - L2
        # เงื่อนไขเมื่อดันจนพื้นที่ใดเหลือน้อยกว่า 1
        if wA < 1 or wB < 1 or wC < 1:
            return "ภารกิจล้มเหลว"
            
    return f"{L1} {L2 - L1} {total - L2}"