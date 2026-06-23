import streamlit as st
import time
import random
import math

st.title("🐔 Đấu Trường Đá Gà Máu Lửa")

st.markdown("""
    <style>
    .arena { width: 400px; height: 400px; border: 10px solid #5d4037;
             border-radius: 50%; background-color: #f1f8e9;
             position: relative; margin: 0 auto; }
    .chicken { width: 30px; height: 30px; border-radius: 50%;
               position: absolute; transition: all 0.05s linear; }
    </style>
""", unsafe_allow_html=True)

if st.button("Bắt đầu trận đấu!"):
    # Vị trí bắt đầu
    c1 = {'x': 100, 'y': 200, 'color': 'red'}
    c2 = {'x': 300, 'y': 200, 'color': 'blue'}
    
    arena_placeholder = st.empty()
    start_time = time.time()
    
    while time.time() - start_time < 30:
        # Tính khoảng cách giữa 2 con
        dx = c2['x'] - c1['x']
        dy = c2['y'] - c1['y']
        dist = math.sqrt(dx**2 + dy**2)
        
        # Nếu ở xa, lao vào nhau; nếu gần, húc mạnh vào nhau
        speed = 15 if dist > 50 else 30 
        
        # Di chuyển hướng về phía nhau (có thêm độ nhiễu để nhìn như đang đá)
        c1['x'] += (dx/dist) * speed + random.randint(-10, 10)
        c1['y'] += (dy/dist) * speed + random.randint(-10, 10)
        c2['x'] -= (dx/dist) * speed + random.randint(-10, 10)
        c2['y'] -= (dy/dist) * speed + random.randint(-10, 10)
        
        # Giới hạn trong sân tròn
        for c in [c1, c2]:
            d_center = math.sqrt((c['x']-200)**2 + (c['y']-200)**2)
            if d_center > 185: # Nếu chạm tường thì bật ngược lại vào tâm
                c['x'] = 200 - (c['x']-200) * 0.9
                c['y'] = 200 - (c['y']-200) * 0.9
        
        # Vẽ
        html = f'''
        <div class="arena">
            <div class="chicken" style="left:{c1['x']}px; top:{c1['y']}px; background-color:red;"></div>
            <div class="chicken" style="left:{c2['x']}px; top:{c2['y']}px; background-color:blue;"></div>
        </div>
        '''
        arena_placeholder.markdown(html, unsafe_allow_html=True)
        time.sleep(0.05)
    
    st.success("Trận đấu kết thúc! Gà nào cũng tơi tả!")
