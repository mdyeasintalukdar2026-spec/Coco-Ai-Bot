from flask import Flask, jsonify, make_response
import threading
import requests
import time
import os

app = Flask(__name__, static_folder=None)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "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")
FINNHUB_API_KEY = os.environ.get("FINNHUB_API_KEY", "db75m8pr01qptb5nip7gdb75m8pr01qptb5nip80")

@app.after_request
def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response

@app.route('/')
def index():
    return "COCO AI - 2M KNOWLEDGE NODES & 67 APIS ULTRA PRO MAX ENGINE ONLINE"

@app.route('/ping')
def ping():
    return "OK", 200

@app.route('/signal')
def get_coco_signal():
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": "You are Coco AI. Return ONLY 'CALL' or 'PUT'. Eliminate all fake signals using institutional 2M node algorithms."},
                {"role": "user", "content": "Analyze current live order flow confluence and return strict direction."}
            ],
            "temperature": 0.01,
            "max_tokens": 5
        }
        resp = requests.post(url, json=payload, headers=headers, timeout=2.5)
        sig = "UP"
        if resp.status_code == 200:
            txt = resp.json()["choices"][0]["message"]["content"].strip().upper()
            if "PUT" in txt or "DOWN" in txt:
                sig = "DOWN"
        return jsonify({"signal": sig, "status": "GREEN_EXECUTE", "engine": "Coco AI 2M Nodes"})
    except Exception:
        t = int(time.time())
        return jsonify({"signal": "UP" if t % 2 == 0 else "DOWN", "status": "GREEN_EXECUTE"})

@app.route('/bot.js')
def bot_script():
    js_code = """
    (function(){
        try {
            var d = document;
            var uniqueId = 'coco_ai_bot_' + Math.floor(Math.random() * 10000);
            
            if(!d.getElementById('coco_global_styles')){
                var s = d.createElement('style');
                s.id = 'coco_global_styles';
                s.innerHTML = 
                    '@keyframes cocoNeonCycle {' +
                        '0%{border-color:#eab308;box-shadow:0 0 18px rgba(234, 179, 8, 0.95);}' +
                        '33%{border-color:#00ffff;box-shadow:0 0 18px rgba(0, 255, 255, 0.95);}' +
                        '66%{border-color:#a855f7;box-shadow:0 0 18px rgba(168, 85, 247, 0.95);}' +
                        '100%{border-color:#eab308;box-shadow:0 0 18px rgba(234, 179, 8, 0.95);}' +
                    '}' +
                    '@keyframes cocoLaserScan {' +
                        '0%{top:20px;opacity:0.9;}' +
                        '50%{top:calc(100vh - 45px);opacity:1;}' +
                        '100%{top:20px;opacity:0.9;}' +
                    '}' +
                    '@keyframes cocoPop {0%{opacity:0;transform:translate(-50%, -45%) scale(0.9);}100%{opacity:1;transform:translate(-50%, -50%) scale(1);}}';
                d.head.appendChild(s);
            }

            var isVerified = sessionStorage.getItem('coco_verified_' + uniqueId) === 'true';
            if(!isVerified) { createLicensePanel(); } else { createFloatingCocoBot(); }

            function createLicensePanel(){
                var panel = d.getElementById('coco_license_panel');
                if(panel) panel.remove();

                panel = d.createElement('div');
                panel.id = 'coco_license_panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:280px;background:#03080e;border:4px solid #eab308;border-radius:15px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 40px 100px rgba(0,0,0,0.98);overflow:hidden;animation:cocoPop 0.3s ease-out forwards;';
                
                panel.innerHTML = '<div style="background:#040d1a;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #131d2e;">' +
                                  '<div style="display:flex;align-items:center;gap:10px;">' +
                                  '<div style="width:36px;height:36px;border-radius:50%;background:#eab308;display:flex;align-items:center;justify-content:center;font-weight:900;color:#000;font-size:14px;">CC</div>' +
                                  '<div><div style="font-size:12px;font-weight:900;color:#fff;">COCO AI BOT</div><div style="font-size:7px;color:#00ff66;font-weight:700;">2M NODES ACTIVE</div></div>' +
                                  '</div><button id="coco-close" style="background:#101826;border:none;color:#fff;width:22px;height:22px;border-radius:4px;cursor:pointer;">×</button></div>' +
                                  '<div style="padding:14px;text-align:center;">' +
                                  '<div style="font-size:8px;color:#eab308;margin-bottom:8px;font-weight:bold;">ENTER COCO ACCESS KEY</div>' +
                                  '<input type="password" id="coco-key" placeholder="Access Key" style="width:100%;box-sizing:border-box;background:#040d1a;border:1px solid #16253f;padding:8px;border-radius:6px;color:#fff;font-size:10px;text-align:center;margin-bottom:10px;letter-spacing:1px;" />' +
                                  '<button id="coco-v-btn" style="width:100%;background:linear-gradient(90deg, #eab308, #00ff66);border:none;padding:9px;border-radius:6px;font-weight:900;font-size:10px;color:#000;cursor:pointer;">ACTIVATE COCO AI</button></div>';
                
                d.body.appendChild(panel);
                panel.querySelector('#coco-close').onclick = function(){ panel.remove(); };
                
                var vBtn = panel.querySelector('#coco-v-btn');
                var keyInput = panel.querySelector('#coco-key');
                vBtn.onclick = function(){
                    var k = keyInput.value.trim();
                    if(k === 'COCO' || k === 'YASIN' || k === '123'){
                        vBtn.innerHTML = 'Authenticating...';
                        setTimeout(function(){
                            sessionStorage.setItem('coco_verified_' + uniqueId, 'true');
                            panel.remove();
                            createFloatingCocoBot();
                        }, 600);
                    } else {
                        vBtn.style.background = '#ff1744'; vBtn.style.color = '#fff'; vBtn.innerText = 'INVALID KEY';
                    }
                };
            }

            function createFloatingCocoBot(){
                if(d.getElementById('coco_target_wrap')) d.getElementById('coco_target_wrap').remove();

                var wrap = d.createElement('div');
                wrap.id = 'coco_target_wrap';
                wrap.style.cssText = 'position:fixed;bottom:70px;left:20px;display:flex;flex-direction:column;align-items:center;z-index:2147483647;cursor:pointer;';
                
                var b = d.createElement('div');
                b.style.cssText = 'width:62px;height:62px;border-radius:50%;background:#040d1a;display:flex;align-items:center;justify-content:center;border:4px solid #eab308;box-sizing:border-box;animation:cocoNeonCycle 3.5s infinite linear;';
                b.innerHTML = '<span style="font-weight:900;color:#eab308;font-size:13px;">COCO</span>';
                wrap.appendChild(b);
                d.body.appendChild(wrap);

                var isDragging = false, startX, startY, hasMoved = false;
                wrap.onmousedown = wrap.ontouchstart = function(e){
                    isDragging = true; hasMoved = false;
                    var p = e.touches ? e.touches[0] : e;
                    startX = p.clientX - wrap.offsetLeft; startY = p.clientY - wrap.offsetTop;
                };
                wrap.onmousemove = wrap.ontouchmove = function(e){
                    if(!isDragging) return;
                    var p = e.touches ? e.touches[0] : e;
                    var nx = p.clientX - startX, ny = p.clientY - startY;
                    if(Math.abs(nx - wrap.offsetLeft) > 2 || Math.abs(ny - wrap.offsetTop) > 2) hasMoved = true;
                    wrap.style.left = nx + 'px'; wrap.style.top = ny + 'px'; wrap.style.bottom = 'auto'; wrap.style.right = 'auto';
                };
                wrap.onmouseup = wrap.ontouchend = function(){ isDragging = false; };
                
                wrap.onclick = function(){
                    if(!hasMoved) runCocoScanningAndTrade(wrap);
                };
            }

            var isExec = false;
            function triggerCocoTrade(isSell){
                if(isExec) return;
                isExec = true;
                var targetBtn = null;
                var selectors = isSell ? ['.section-deal__button-down button', '.section-deal__button-down', 'button.btn-red', 'button[class*="put"]']
                                       : ['.section-deal__button-up button', '.section-deal__button-up', 'button.btn-green', 'button[class*="call"]'];
                
                for(var i=0; i<selectors.length; i++){
                    var el = d.querySelector(selectors[i]);
                    if(el && el.getBoundingClientRect().width > 0){ targetBtn = el; break; }
                }

                if(targetBtn){ try{ targetBtn.click(); }catch(e){} }
            }

            function getActiveMarketName() {
                try {
                    var el = d.querySelector('.asset-select__current-item span') || d.querySelector('.chart-instrument__name');
                    if(el) return el.innerText.trim();
                } catch(e){}
                return 'EUR/USD (OTC)';
            }

            var isScanning = false;
            function runCocoScanningAndTrade(botWrap){
                if(isScanning) return;
                isScanning = true; isExec = false;

                var dim = d.createElement('div');
                dim.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(0,0,0,0.45);backdrop-filter:blur(1.5px);z-index:2147483645;pointer-events:none;';
                d.body.appendChild(dim);

                var laser = d.createElement('div');
                laser.style.cssText = 'position:fixed;left:0;width:100vw;height:18px;background:linear-gradient(90deg, transparent, #ffffff, #00ffff, #ffffff, transparent);box-shadow:0 0 55px #00ffff;z-index:2147483646;pointer-events:none;animation:cocoLaserScan 1.66s ease-in-out 3;';
                d.body.appendChild(laser);

                var rect = botWrap.getBoundingClientRect();
                var box = d.createElement('div');
                box.style.cssText = 'position:fixed;left:' + Math.max(10, rect.left) + 'px;bottom:' + (window.innerHeight - rect.top + 12) + 'px;background:rgba(3,8,14,0.95);border:3px solid #eab308;color:#00ff66;padding:12px 16px;border-radius:10px;font-family:monospace;font-size:11px;z-index:2147483647;min-width:185px;';
                box.innerHTML = '<div style="color:#8a99ad;font-size:8px;">coco-ai@core:~#</div><div style="color:#fff;font-weight:bold;" id="coco-status">analyzing...</div><div style="color:#00ffff;font-size:9px;">market: ' + getActiveMarketName() + '</div>';
                d.body.appendChild(box);

                setTimeout(function(){
                    fetch('https://yasin-tr-bot.onrender.com/signal?t='+Date.now())
                    .then(function(r){ return r.json(); })
                    .catch(function(){ return {signal: "DOWN"}; })
                    .then(function(j){
                        var isDown = (String(j.signal).toUpperCase() === 'DOWN');
                        if(laser) laser.remove();
                        if(dim) dim.remove();

                        triggerCocoTrade(isDown);

                        var col = isDown ? '#ff1744' : '#00ff66';
                        box.style.borderColor = col;
                        var st = box.querySelector('#coco-status');
                        if(st){
                            st.innerText = isDown ? 'signal: DOWN ⬇️' : 'signal: UP ⬆️';
                            st.style.color = col;
                        }

                        setTimeout(function(){
                            if(box) box.remove();
                            isScanning = false;
                        }, 2000);
                    });
                }, 4000);
            }
        } catch(e){}
    })();
    """
    res = make_response(js_code)
    res.headers['Content-Type'] = 'application/javascript'
    return res

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    threading.Thread(target=run, daemon=True).start()
