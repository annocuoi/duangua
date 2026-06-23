import streamlit as st
import time
import random
import math

st.set_page_config(page_title="Đấu Trường Đá Gà", layout="centered")
st.title("🐔 Đấu Trường Đá Gà Máu Lửa")

# CSS: Thêm vạch xuất phát
st.markdown("""
    <style>
    .arena { width: 400px; height: 400px; border: 10px solid #5d4037;
             border-radius: 50%; background-color: #f1f8e9;
             position: relative; margin: 0 auto; overflow: hidden; }
    .line { position: absolute; width: 40px; height: 5px; background: white; }
    .chicken { width: 30px; height: 30px; border-radius: 50%;
               position: absolute; transition: all 0.05s linear; 
               box-shadow: 0 0 10px rgba(0,0,0,0.3); }
    </style>
""", unsafe_allow_html=True)

if st.button("Bắt đầu trận đấu!"):
    # Kết quả (10% Hòa, 45% Đỏ, 45% Xanh)
    rand = random.random()
    result = "Hòa" if rand < 0.10 else ("Đỏ Thắng" if rand < 0.55 else "Xanh Thắng")
        
    # Vị trí xuất phát đối xứng
    c1 = {'x': 200, 'y': 80, 'color': 'red', 'bias': 1.2 if result == "Đỏ Thắng" else 0.8}
    c2 = {'x': 200, 'y': 320, 'color': 'blue', 'bias': 1.2 if result == "Xanh Thắng" else 0.8}
    
    arena_placeholder = st.empty()
    start_time = time.time()
    
    while time.time() - start_time < 60: # Trận đấu kéo dài 60s
        dx = c2['x'] - c1['x']
        dy = c2['y'] - c1['y']
        dist = math.sqrt(dx**2 + dy**2)
        
        # VA CHẠM: Nếu khoảng cách < 60px thì giảm tốc độ (đang "đá")
        # Nếu ở xa thì lao vào nhau nhanh
        speed = 5 if dist < 60 else 25
        
        # Di chuyển
        c1['x'] += (dx/dist) * speed * c1['bias'] + random.randint(-15, 15)
        c1['y'] += (dy/dist) * speed * c1['bias'] + random.randint(-15, 15)
        c2['x'] -= (dx/dist) * speed * c2['bias'] + random.randint(-15, 15)
        c2['y'] -= (dy/dist) * speed * c2['bias'] + random.randint(-15, 15)
        
        # Ép trong sân
        for c in [c1, c2]:
            d_center = math.sqrt((c['x']-200)**2 + (c['y']-200)**2)
            if d_center > 170:
                angle = math.atan2(c['y']-200, c['x']-200)
                c['x'] = 200 + 165 * math.cos(angle)
                c['y'] = 200 + 165 * math.sin(angle)
        
        # Hiển thị vạch xuất phát + gà
        html = f'''
        <div class="arena">
            <div class="line" style="left:180px; top:80px;"></div>
            <div class="line" style="left:180px; top:320px;"></div>
            <div class="chicken" style="left:{c1['x']}px; top:{c1['y']}px; background-color:red;"></div>
            <div class="chicken" style="left:{c2['x']}px; top:{c2['y']}px; background-color:blue;"></div>
        </div>
        '''
        arena_placeholder.markdown(html, unsafe_allow_html=True)
        time.sleep(0.05)
    
    # Kết quả
    if result == "Hòa": st.warning("HÒA - Cả hai chiến kê đều kiệt sức!")
    elif result == "Đỏ Thắng": st.error("ĐỎ THẮNG - Một trận đấu mãn nhãn!")
    else: st.info("XANH THẮNG - Đòn đá chí mạng!")
