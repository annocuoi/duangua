import streamlit as st
import time
import random
import math

st.set_page_config(page_title="Đấu Trường Đá Gà", layout="centered")
st.title("🐔 Đấu Trường Đá Gà Máu Lửa")

# CSS tạo sân đấu và chiến kê
st.markdown("""
    <style>
    .arena { width: 400px; height: 400px; border: 10px solid #5d4037;
             border-radius: 50%; background-color: #f1f8e9;
             position: relative; margin: 0 auto; overflow: hidden; }
    .chicken { width: 30px; height: 30px; border-radius: 50%;
               position: absolute; transition: all 0.05s linear; 
               box-shadow: 0 0 10px rgba(0,0,0,0.3); }
    </style>
""", unsafe_allow_html=True)

if st.button("Bắt đầu trận đấu!"):
    # 1. Quyết định kết quả (10% Hòa, 45% Đỏ thắng, 45% Xanh thắng)
    rand = random.random()
    if rand < 0.10: result = "Hòa"
    elif rand < 0.55: result = "Đỏ Thắng"
    else: result = "Xanh Thắng"
        
    c1 = {'x': 100, 'y': 200, 'color': 'red', 'bias': 1.2 if result == "Đỏ Thắng" else 0.8}
    c2 = {'x': 300, 'y': 200, 'color': 'blue', 'bias': 1.2 if result == "Xanh Thắng" else 0.8}
    
    arena_placeholder = st.empty()
    start_time = time.time()
    
    while time.time() - start_time < 30:
        dx = c2['x'] - c1['x']
        dy = c2['y'] - c1['y']
        dist = math.sqrt(dx**2 + dy**2)
        
        # Nếu quá gần thì húc mạnh, nếu xa thì lao tới
        speed = 40 if dist < 60 else 20
        
        # Di chuyển có hướng về phía nhau + bias (lợi thế cho gà thắng)
        c1['x'] += (dx/dist) * speed * c1['bias'] + random.randint(-15, 15)
        c1['y'] += (dy/dist) * speed * c1['bias'] + random.randint(-15, 15)
        c2['x'] -= (dx/dist) * speed * c2['bias'] + random.randint(-15, 15)
        c2['y'] -= (dy/dist) * speed * c2['bias'] + random.randint(-15, 15)
        
        # Ép buộc vào sân tròn
        for c in [c1, c2]:
            d_center = math.sqrt((c['x']-200)**2 + (c['y']-200)**2)
            if d_center > 170:
                angle = math.atan2(c['y']-200, c['x']-200)
                c['x'] = 200 + 165 * math.cos(angle)
                c['y'] = 200 + 165 * math.sin(angle)
        
        # Hiển thị
        html = f'''
        <div class="arena">
            <div class="chicken" style="left:{c1['x']}px; top:{c1['y']}px; background-color:red;"></div>
            <div class="chicken" style="left:{c2['x']}px; top:{c2['y']}px; background-color:blue;"></div>
        </div>
        '''
        arena_placeholder.markdown(html, unsafe_allow_html=True)
        time.sleep(0.05)
    
    # Công bố kết quả
    if result == "Hòa": st.warning("Trận đấu quá ngang tài ngang sức! KẾT QUẢ: HÒA")
    elif result == "Đỏ Thắng": st.error("Gà Đỏ tung cú đá quyết định! ĐỎ THẮNG")
    else: st.info("Gà Xanh chiếm ưu thế tuyệt đối! XANH THẮNG")
