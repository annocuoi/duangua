import streamlit as st
import time
import random
import math

st.set_page_config(page_title="Đấu Trường Đá Gà", layout="centered")
st.title("🐔 Đấu Trường Đá Gà Máu Lửa")

st.markdown("""
    <style>
    .arena { width: 400px; height: 400px; border: 10px solid #5d4037;
             border-radius: 50%; background-color: #f1f8e9;
             position: relative; margin: 0 auto; overflow: hidden; }
    .line { position: absolute; width: 60px; height: 10px; background: white; 
            box-shadow: 0 0 5px rgba(0,0,0,0.5); border-radius: 2px; }
    .chicken { width: 30px; height: 30px; border-radius: 50%;
               position: absolute; transition: all 0.05s linear; }
    </style>
""", unsafe_allow_html=True)

# Khởi tạo trạng thái
if 'running' not in st.session_state: st.session_state.running = False
if 'result' not in st.session_state: st.session_state.result = None

def start_game():
    st.session_state.running = True
    st.session_state.result = None # Xóa kết quả cũ

# Giao diện nút bấm
if not st.session_state.running:
    st.button("Bắt đầu trận đấu!", on_click=start_game)
else:
    st.button("Đang chiến đấu...", disabled=True)

# Logic game
if st.session_state.running:
    rand = random.random()
    res = "Hòa" if rand < 0.10 else ("Đỏ Thắng" if rand < 0.55 else "Xanh Thắng")
    
    c1 = {'x': 200, 'y': 80, 'color': 'red', 'bias': 1.2 if res == "Đỏ Thắng" else 0.8}
    c2 = {'x': 200, 'y': 320, 'color': 'blue', 'bias': 1.2 if res == "Xanh Thắng" else 0.8}
    
    arena_placeholder = st.empty()
    start_time = time.time()
    is_fighting = False
    
    # Giảm thời gian xuống 30 giây
    while time.time() - start_time < 30:
        dx = c2['x'] - c1['x']
        dy = c2['y'] - c1['y']
        dist = math.sqrt(dx**2 + dy**2)
        
        speed = 1.5 if (dist > 80 and not is_fighting) else (25 if dist > 60 else 5)
        if dist <= 80: is_fighting = True
        
        c1['x'] += (dx/dist) * speed * c1['bias'] + random.randint(-5, 5)
        c1['y'] += (dy/dist) * speed * c1['bias'] + random.randint(-5, 5)
        c2['x'] -= (dx/dist) * speed * c2['bias'] + random.randint(-15, 15)
        c2['y'] -= (dy/dist) * speed * c2['bias'] + random.randint(-15, 15)
        
        # Ép trong sân
        for c in [c1, c2]:
            d_center = math.sqrt((c['x']-200)**2 + (c['y']-200)**2)
            if d_center > 170:
                angle = math.atan2(c['y']-200, c['x']-200)
                c['x'] = 200 + 165 * math.cos(angle)
                c['y'] = 200 + 165 * math.sin(angle)
        
        html = f'''
        <div class="arena">
            <div class="line" style="left:170px; top:80px;"></div>
            <div class="line" style="left:170px; top:320px;"></div>
            <div class="chicken" style="left:{c1['x']}px; top:{c1['y']}px; background-color:red;"></div>
            <div class="chicken" style="left:{c2['x']}px; top:{c2['y']}px; background-color:blue;"></div>
        </div>
        '''
        arena_placeholder.markdown(html, unsafe_allow_html=True)
        time.sleep(0.05)
    
    # Kết thúc: Lưu kết quả vào session_state để không bị mất
    st.session_state.running = False
    st.session_state.result = res
    st.rerun()

# Hiển thị kết quả lưu từ session_state
if st.session_state.result:
    res = st.session_state.result
    if res == "Hòa": st.warning("HÒA - Cả hai chiến kê đều kiệt sức!")
    elif res == "Đỏ Thắng": st.error("ĐỎ THẮNG - Một trận đấu mãn nhãn!")
    else: st.info("XANH THẮNG - Đòn đá chí mạng!")
