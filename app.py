from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="te">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pratap Edits | Professional Video & Photo Editing in Nandigama</title>
    <meta name="title" content="Pratap Edits">
    <meta name="description" content="Official website of Pratap Edits by Achi Pratap, Nandigama. Best video editing, photo editing, movie clips, and audio editing services at ₹30 per clip. Call: 9704824658.">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {
            --bg-grad: linear-gradient(135deg, #1e1b4b 0%, #311042 35%, #0f172a 70%, #064e3b 100%);
            --card-bg: rgba(255, 255, 255, 0.07);
            --text-light: #ffffff;
            --text-muted: #e2e8f0;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif; }

        body {
            background: var(--bg-grad);
            background-attachment: fixed;
            color: var(--text-light);
            min-height: 100vh;
            padding-bottom: 60px;
        }

        header {
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(12px);
            position: sticky;
            top: 0;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 20px;
            border-bottom: 3px solid;
            border-image: linear-gradient(90deg, #10b981, #3b82f6, #ec4899, #8b5cf6) 1;
        }

        .logo-area h1 {
            font-size: 1.5rem;
            font-weight: 800;
            background: linear-gradient(45deg, #10b981, #38bdf8, #f472b6, #fbbf24);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .menu-btn {
            background: linear-gradient(45deg, #3b82f6, #8b5cf6);
            border: none;
            color: white;
            padding: 8px 14px;
            border-radius: 10px;
            font-size: 1.2rem;
            cursor: pointer;
        }

        .container { max-width: 650px; margin: 20px auto; padding: 0 15px; }

        .search-box { position: relative; margin-bottom: 20px; }
        .search-box input {
            width: 100%;
            padding: 14px 15px 14px 50px;
            background: rgba(15, 23, 42, 0.7);
            border: 2px solid #3b82f6;
            border-radius: 15px;
            color: white;
            font-size: 1rem;
            outline: none;
        }
        .search-box i { position: absolute; left: 18px; top: 50%; transform: translateY(-50%); color: #38bdf8; font-size: 1.2rem; }

        .categories { display: flex; gap: 12px; overflow-x: auto; padding-bottom: 10px; margin-bottom: 25px; }
        .categories::-webkit-scrollbar { display: none; }
        .cat-chip {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 10px 18px;
            border-radius: 25px;
            white-space: nowrap;
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            color: var(--text-muted);
        }
        .cat-chip.active { 
            background: linear-gradient(45deg, #10b981, #3b82f6); 
            color: white; 
            border: none;
        }

        .card {
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 22px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.4);
            margin-bottom: 25px;
        }

        .form-group { margin-bottom: 18px; }
        .form-group label { display: block; font-size: 0.9rem; margin-bottom: 8px; color: #34d399; font-weight: 600; }
        .form-control {
            width: 100%; padding: 12px 15px;
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            color: white; font-size: 0.95rem; outline: none;
        }

        .price-tag {
            background: linear-gradient(45deg, rgba(16, 185, 129, 0.2), rgba(59, 130, 246, 0.2));
            border: 2px dashed #fbbf24;
            padding: 15px; border-radius: 12px;
            text-align: center; margin-bottom: 20px;
            font-weight: 700; font-size: 1.1rem; color: #fef08a;
        }

        .btn-submit {
            width: 100%; padding: 14px;
            background: linear-gradient(45deg, #10b981, #3b82f6, #8b5cf6);
            border: none; border-radius: 12px;
            color: white; font-weight: 700; font-size: 1.05rem; cursor: pointer;
        }

        .drawer {
            position: fixed; top: 0; right: -300px; width: 300px; height: 100%;
            background: linear-gradient(180deg, #1e1b4b, #064e3b);
            border-left: 3px solid #10b981;
            z-index: 2000; transition: 0.4s ease; padding: 25px;
        }
        .drawer.open { right: 0; }
        .drawer-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 15px; }
        .drawer-item { 
            padding: 14px; margin-bottom: 12px; border-radius: 12px; 
            background: rgba(255,255,255,0.1); cursor: pointer; display: flex; align-items: center; gap: 12px; 
            font-weight: 500; border: 1px solid rgba(255,255,255,0.1);
        }

        .overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); display: none; z-index: 1500; }
        .overlay.show { display: block; }

        .modal {
            display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
            background: #1e1b4b; border: 2px solid #3b82f6; width: 90%; max-width: 420px;
            padding: 25px; border-radius: 20px; z-index: 3000;
        }
        .modal.show { display: block; }

        #adminDashboard { display: none; }
        .stats-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 20px; }
        .stat-card { background: rgba(255, 255, 255, 0.08); padding: 15px; border-radius: 12px; text-align: center; border: 1px solid #10b981; }
        .table-responsive { overflow-x: auto; margin-top: 15px; }
        table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
        th, td { border: 1px solid rgba(255,255,255,0.2); padding: 10px; text-align: left; }
        th { background: #059669; color: white; }
    </style>
</head>
<body>

    <header>
        <div class="logo-area"><h1>ప్రతాప్ ఎడిట్స్</h1></div>
        <button class="menu-btn" onclick="toggleDrawer()"><i class="fa-solid fa-bars-staggered"></i></button>
    </header>

    <div class="container">
        <div class="search-box">
            <i class="fa-solid fa-wand-magic-sparkles"></i>
            <input type="text" id="searchInput" placeholder="వీడియో, ఫోటో లేదా ఆడియో ఎడిటింగ్ వెతకండి...">
        </div>

        <div class="categories">
            <div class="cat-chip active" onclick="selectCat(this)">✨ అన్నీ (All)</div>
            <div class="cat-chip" onclick="selectCat(this)">🎬 వీడియో ఎడిటింగ్</div>
            <div class="cat-chip" onclick="selectCat(this)">🖼️ ఫోటో ఎడిటింగ్</div>
            <div class="cat-chip" onclick="selectCat(this)">🍿 మూవీ క్లిప్స్</div>
            <div class="cat-chip" onclick="selectCat(this)">🎵 ఆడియో ఎడిటింగ్</div>
        </div>

        <!-- Booking Form -->
        <div class="card">
            <h2 style="font-size: 1.2rem; margin-bottom: 18px; color: #34d399;"><i class="fa-solid fa-pen-nib"></i> ఎడిటింగ్ బుకింగ్ ఫారం</h2>
            <form id="bookingForm" onsubmit="submitBooking(event)">
                <div class="form-group">
                    <label>మీ పేరు (Name)</label>
                    <input type="text" id="clientName" class="form-control" required placeholder="మీ పూర్తి పేరు రాయండి">
                </div>
                <div class="form-group">
                    <label>ఫోన్ నెంబర్ (Phone Number)</label>
                    <input type="tel" id="clientPhone" class="form-control" required placeholder="10 అంకెల ఫోన్ నెంబర్">
                </div>
                <div class="form-group">
                    <label>ఎడిటింగ్ రకం (Editing Type)</label>
                    <select id="editType" class="form-control">
                        <option value="Video Editing" style="background:#0f172a;">🎬 వీడియో ఎడిటింగ్</option>
                        <option value="Photo Editing" style="background:#0f172a;">🖼️ ఫోటో ఎడిటింగ్</option>
                        <option value="Movie Clips" style="background:#0f172a;">🍿 మూవీ క్లిప్స్</option>
                        <option value="Audio Editing" style="background:#0f172a;">🎵 ఆడియో ఎడిటింగ్</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>క్లిప్స్ / ఫైల్స్ సంఖ్య (Clips Count)</label>
                    <input type="number" id="clipCount" class="form-control" value="1" min="1" oninput="calculatePrice()">
                </div>
                <div class="form-group">
                    <label>అప్‌లోడ్ ఫైల్ (Upload File)</label>
                    <input type="file" id="mediaFile" class="form-control" multiple>
                </div>
                <div class="price-tag" id="priceDisplay">💰 మొత్తం ధర: ₹30 (ఒక్కో ఎడిటింగ్ ₹30)</div>
                <button type="submit" class="btn-submit">🚀 బుక్ చేయండి & WhatsApp కి పంపండి</button>
            </form>
        </div>

        <!-- Admin Login -->
        <div class="card" id="loginCard">
            <h3 style="font-size: 1.1rem; margin-bottom: 15px; color: #f472b6;"><i class="fa-solid fa-lock"></i> అడ్మిన్ లాగిన్</h3>
            <form onsubmit="adminLogin(event)">
                <div class="form-group">
                    <label style="color: #f472b6;">యూజర్నేమ్</label>
                    <input type="text" id="adminUser" class="form-control" placeholder="యూజర్నేమ్ టైప్ చేయండి" required>
                </div>
                <div class="form-group">
                    <label style="color: #f472b6;">పాస్‌వర్డ్</label>
                    <input type="password" id="adminPass" class="form-control" placeholder="పాస్‌వర్డ్ టైప్ చేయండి" required>
                </div>
                <button type="submit" class="btn-submit" style="background: linear-gradient(45deg, #ec4899, #8b5cf6);">🔑 లాగిన్ అవ్వండి</button>
            </form>
        </div>

        <!-- Admin Dashboard -->
        <div class="card" id="adminDashboard">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <h3 style="color: #fbbf24;"><i class="fa-solid fa-chart-line"></i> అడ్మిన్ డ్యాష్‌బోర్డ్</h3>
                <button onclick="adminLogout()" style="background: #ef4444; border: none; color: white; padding: 6px 12px; border-radius: 8px; font-weight: 600; cursor: pointer;">లాగౌట్</button>
            </div>
            <div class="stats-grid">
                <div class="stat-card">
                    <h4>మొత్తం బుకింగ్స్</h4>
                    <p id="totalBookingsCount" style="font-size: 1.4rem; font-weight: 700; color: #fbbf24;">0</p>
                </div>
                <div class="stat-card">
                    <h4>అంచనా ఆదాయం</h4>
                    <p id="totalRevenue" style="font-size: 1.4rem; font-weight: 700; color: #34d399;">₹0</p>
                </div>
            </div>
            <h4 style="color: #38bdf8; margin-bottom: 10px;">ఆర్డర్ల వివరాలు:</h4>
            <div class="table-responsive">
                <table>
                    <thead>
                        <tr>
                            <th>పేరు</th>
                            <th>ఫోన్</th>
                            <th>రకం</th>
                            <th>క్లిప్స్</th>
                            <th>ధర</th>
                        </tr>
                    </thead>
                    <tbody id="bookingsTableBody"></tbody>
                </table>
            </div>
        </div>

    </div>

    <!-- Sidebar Drawer -->
    <div class="drawer" id="sideDrawer">
        <div class="drawer-header">
            <h3 style="color: #34d399;">మెనూ Options</h3>
            <button class="menu-btn" onclick="toggleDrawer()"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <div class="drawer-item" onclick="makeCall()"><i class="fa-solid fa-phone" style="color: #34d399;"></i> టాక్ టు ఎడిటర్</div>
        <div class="drawer-item" onclick="openModal('editorModal')"><i class="fa-solid fa-id-card" style="color: #38bdf8;"></i> ఎడిటర్ డీటెయిల్స్</div>
        <div class="drawer-item" onclick="openModal('complaintModal')"><i class="fa-solid fa-circle-exclamation" style="color: #f87171;"></i> రైజ్ ఏ కంప్లైంట్</div>
    </div>
    <div class="overlay" id="drawerOverlay" onclick="toggleDrawer()"></div>

    <!-- Modals -->
    <div class="modal" id="editorModal">
        <h3 style="color: #38bdf8; margin-bottom: 15px;">👤 ఎడిటర్ వివరాలు</h3>
        <p style="margin-bottom: 20px; font-size: 0.95rem; line-height: 1.8; color: var(--text-muted);">
            <b>పేరు:</b> అచ్చి ప్రతాప్<br>
            <b>చిరునామా:</b> DVR కాలనీ రోడ్డు, నందిగామ, PIN: 521185.<br>
            <b>ఫోన్ నెంబర్:</b> 9704824658
        </p>
        <button class="btn-submit" onclick="closeModal('editorModal')">ఓకే</button>
    </div>

    <div class="modal" id="complaintModal">
        <h3 style="color: #f87171; margin-bottom: 15px;">⚠️ ఫిర్యాదు చేయండి</h3>
        <form onsubmit="submitComplaint(event)">
            <div class="form-group">
                <input type="text" id="compName" class="form-control" placeholder="మీ పేరు" required>
            </div>
            <div class="form-group">
                <textarea id="compText" class="form-control" rows="3" placeholder="మీ సమస్యను టైప్ చేయండి..." required></textarea>
            </div>
            <button type="submit" class="btn-submit" style="background: linear-gradient(45deg, #ef4444, #ec4899);">సబ్మిట్ చేయండి</button>
        </form>
        <button class="btn-submit" style="background: #475569; margin-top: 10px;" onclick="closeModal('complaintModal')">రద్దు</button>
    </div>

    <!-- JavaScript -->
    <script>
        let bookingsData = [];

        function toggleDrawer() {
            document.getElementById('sideDrawer').classList.toggle('open');
            document.getElementById('drawerOverlay').classList.toggle('show');
        }

        function openModal(modalId) {
            toggleDrawer();
            document.getElementById(modalId).classList.add('show');
            document.getElementById('drawerOverlay').classList.add('show');
        }

        function closeModal(modalId) {
            document.getElementById(modalId).classList.remove('show');
            document.getElementById('drawerOverlay').classList.remove('show');
        }

        function makeCall() { window.location.href = 'tel:9704824658'; }

        function calculatePrice() {
            let count = document.getElementById('clipCount').value || 1;
            let total = count * 30;
            document.getElementById('priceDisplay').innerText = `💰 మొత్తం ధర: ₹${total} (ఒక్కో ఎడిటింగ్ ₹30)`;
        }

        function submitBooking(event) {
            event.preventDefault();
            let name = document.getElementById('clientName').value;
            let phone = document.getElementById('clientPhone').value;
            let type = document.getElementById('editType').value;
            let count = parseInt(document.getElementById('clipCount').value);
            let total = count * 30;

            bookingsData.push({name, phone, type, count, total});
            updateAdminDashboard();

            let msg = `కొత్త ఎడిటింగ్ బుకింగ్!%0a%0aపేరు: ${name}%0aఫోన్: ${phone}%0aరకం: ${type}%0aక్లిప్స్: ${count}%0aమొత్తం: ₹${total}`;
            window.open(`https://wa.me/919704824658?text=${msg}`, '_blank');

            alert('బుకింగ్ పూర్తయింది! వివరాలు వాట్సాప్‌కి పంపబడ్డాయి.');
            document.getElementById('bookingForm').reset();
            calculatePrice();
        }

        function submitComplaint(event) {
            event.preventDefault();
            let name = document.getElementById('compName').value;
            let text = document.getElementById('compText').value;

            let msg = `కొత్త కంప్లైంట్!%0a%0aపేరు: ${name}%0aసమస్య: ${text}`;
            window.open(`https://wa.me/919704824658?text=${msg}`, '_blank');
            closeModal('complaintModal');
        }

        function adminLogin(event) {
            event.preventDefault();
            let user = document.getElementById('adminUser').value.trim();
            let pass = document.getElementById('adminPass').value.trim();

            if((user === 'achi pratap' || user === 'achi pratap @ user') && pass === '97048ABDM*') {
                alert('లాగిన్ విజయవంతమైంది!');
                document.getElementById('loginCard').style.display = 'none';
                document.getElementById('adminDashboard').style.display = 'block';
            } else {
                alert('తప్పు డీటెయిల్స్! దయచేసి సరైన యూజర్నేమ్ మరియు పాస్‌వర్డ్ ఇవ్వండి.');
            }
        }

        function adminLogout() {
            document.getElementById('adminDashboard').style.display = 'none';
            document.getElementById('loginCard').style.display = 'block';
            document.getElementById('adminUser').value = '';
            document.getElementById('adminPass').value = '';
        }

        function updateAdminDashboard() {
            document.getElementById('totalBookingsCount').innerText = bookingsData.length;
            let revenue = bookingsData.reduce((sum, item) => sum + item.total, 0);
            document.getElementById('totalRevenue').innerText = `₹${revenue}`;

            let tbody = document.getElementById('bookingsTableBody');
            tbody.innerHTML = '';
            bookingsData.forEach(b => {
                tbody.innerHTML += `<tr><td>${b.name}</td><td>${b.phone}</td><td>${b.type}</td><td>${b.count}</td><td>₹${b.total}</td></tr>`;
            });
        }

        function selectCat(el) {
            document.querySelectorAll('.cat-chip').forEach(c => c.classList.remove('active'));
            el.classList.add('active');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
  
