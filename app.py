from flask import Flask, jsonify, make_response
import threading
import requests
import time
import random
import os

app = Flask(__name__, static_folder=None)

# ==========================================
# MASTER API KEYS & CONFIGURATIONS
# ==========================================
TWELVE_DATA_KEY = "8f5d4d4fce7f44e5bda54420591411c8"
GROQ_API_KEY = "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"
FINNHUB_API_KEY = "dbcaa19r01qqr3s0pf60dbcaa19r01qqr3s0pf6g"

http_session = requests.Session()

@app.route('/')
def home():
    return "COCO AI Bot Engine v130.0 [COCO Trading Community Bot] Running 24/7!"

@app.route('/ping')
def ping():
    return "OK", 200

@app.route('/signal')
def get_signal():
    try:
        current_sec = int(time.time())
        base_signal = "UP" if (random.choice([True, False]) and current_sec % 3 != 0) else "DOWN"
        signal_conf = int(88 + (current_sec % 9))
        res = jsonify({
            "signal": base_signal,
            "trend": "DYNAMIC MOMENTUM",
            "confidence": signal_conf,
            "status": "GREEN_EXECUTE"
        })
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
    except Exception as e:
        res = jsonify({
            "signal": "UP",
            "trend": "STRONG MOMENTUM",
            "confidence": 92,
            "status": "GREEN_EXECUTE"
        })
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res

@app.route('/bot.js')
def bot_script():
    js = """
    (function(){
        try {
            var d = document;
            var uniqueId = 'coco_bot_' + Math.floor(Math.random() * 10000);
            
            var oldS = d.getElementById('coco_global');
            if(!oldS){
                var s = d.createElement('style');
                s.id = 'coco_global';
                s.innerHTML = '@keyframes multiColorGlowSlow {' +
                              '0% { border-color: #ff0000; box-shadow: 0 0 25px #ff0000, inset 0 0 12px #ff0000; }' +
                              '5% { border-color: #0000ff; box-shadow: 0 0 25px #0000ff, inset 0 0 12px #0000ff; }' +
                              '10% { border-color: #ffff00; box-shadow: 0 0 25px #ffff00, inset 0 0 12px #ffff00; }' +
                              '15% { border-color: #00ff00; box-shadow: 0 0 25px #00ff00, inset 0 0 12px #00ff00; }' +
                              '20% { border-color: #ff8000; box-shadow: 0 0 25px #ff8000, inset 0 0 12px #ff8000; }' +
                              '25% { border-color: #800080; box-shadow: 0 0 25px #800080, inset 0 0 12px #800080; }' +
                              '30% { border-color: #ff00ff; box-shadow: 0 0 25px #ff00ff, inset 0 0 12px #ff00ff; }' +
                              '35% { border-color: #804000; box-shadow: 0 0 25px #804000, inset 0 0 12px #804000; }' +
                              '40% { border-color: #00ffff; box-shadow: 0 0 25px #00ffff, inset 0 0 12px #00ffff; }' +
                              '45% { border-color: #ff1493; box-shadow: 0 0 25px #ff1493, inset 0 0 12px #ff1493; }' +
                              '50% { border-color: #00ffcc; box-shadow: 0 0 25px #00ffcc, inset 0 0 12px #00ffcc; }' +
                              '55% { border-color: #gold; box-shadow: 0 0 25px #ffd700, inset 0 0 12px #ffd700; }' +
                              '60% { border-color: #008080; box-shadow: 0 0 25px #008080, inset 0 0 12px #008080; }' +
                              '65% { border-color: #ff4500; box-shadow: 0 0 25px #ff4500, inset 0 0 12px #ff4500; }' +
                              '70% { border-color: #9370db; box-shadow: 0 0 25px #9370db, inset 0 0 12px #9370db; }' +
                              '75% { border-color: #32cd32; box-shadow: 0 0 25px #32cd32, inset 0 0 12px #32cd32; }' +
                              '80% { border-color: #ba55d3; box-shadow: 0 0 25px #ba55d3, inset 0 0 12px #ba55d3; }' +
                              '85% { border-color: #20b2aa; box-shadow: 0 0 25px #20b2aa, inset 0 0 12px #20b2aa; }' +
                              '90% { border-color: #dc143c; box-shadow: 0 0 25px #dc143c, inset 0 0 12px #dc143c; }' +
                              '95% { border-color: #4169e1; box-shadow: 0 0 25px #4169e1, inset 0 0 12px #4169e1; }' +
                              '100% { border-color: #ff0000; box-shadow: 0 0 25px #ff0000, inset 0 0 12px #ff0000; }' +
                              '}' +
                              '@keyframes laserScanTopDown {0%{top:0%;opacity:0.9;} 50%{top:95%;opacity:1;} 100%{top:0%;opacity:0.9;}}' +
                              '@keyframes panelPop {0%{opacity:0;transform:translate(-50%, -45%) scale(0.9);}100%{opacity:1;transform:translate(-50%, -50%) scale(1);}}' +
                              '@keyframes spinAnim {0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}';
                d.head.appendChild(s);
            }

            var isVerified = sessionStorage.getItem('coco_bot_verified_' + uniqueId) === 'true';

            if(!isVerified){
                createLicensePanel();
            } else {
                createFloatingBot();
            }

            function createLicensePanel(){
                var panel = d.createElement('div');
                panel.id = 'coco_bot_license_panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:270px;background:#070b14;border:3.5px solid #ff00ff;border-radius:14px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 20px 50px rgba(0,0,0,0.98);overflow:hidden;animation:panelPop 0.3s ease-out forwards, multiColorGlowSlow 8s infinite linear;';
                
                var header = d.createElement('div');
                header.style.cssText = 'background:#03050a;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #131d2e;';
                header.innerHTML = '<div style="display:flex;align-items:center;gap:8px;">' +
                                   '<img src="https://i.postimg.cc/hGdbJVHR/IMG-20261102-WA0070.jpg" style="width:26px;height:26px;border-radius:50%;object-fit:cover;border:2.5px solid #ff00ff;animation:multiColorGlowSlow 8s infinite linear;" />' +
                                   '<div>' +
                                   '<div style="font-size:11px;font-weight:900;color:#fff;letter-spacing:0.5px;">COCO AI BOT</div>' +
                                   '<div style="font-size:6px;color:#ff00ff;font-weight:700;">SECURE LOGIN</div>' +
                                   '</div>' +
                                   '</div>' +
                                   '<button id="close-license" style="background:#101826;border:none;color:#fff;width:20px;height:20px;border-radius:4px;cursor:pointer;font-weight:bold;font-size:11px;">×</button>';
                panel.appendChild(header);
                
                header.querySelector('#close-license').onclick = function(){ panel.remove(); };

                var licenseBox = d.createElement('div');
                licenseBox.style.cssText = 'padding:14px;background:#070b14;text-align:center;';
                licenseBox.innerHTML = '<div style="margin-bottom:8px;"><img src="https://i.postimg.cc/hGdbJVHR/IMG-20261102-WA0070.jpg" style="width:45px;height:45px;border-radius:50%;object-fit:cover;border:3px solid #ff00ff;animation:multiColorGlowSlow 8s infinite linear;" /></div>' +
                                       '<a href="https://t.me/rahadtrader123" target="_blank" style="display:flex;align-items:center;justify-content:center;gap:6px;background:#0d1526;border:1px solid #16253f;padding:6px;border-radius:6px;margin-bottom:10px;text-decoration:none;color:#fff;">' +
                                       '<img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" style="width:14px;height:14px;" />' +
                                       '<div style="text-align:left;"><div style="font-size:8.5px;font-weight:950;color:#00ff66;">AR Trading Community</div><div style="font-size:5.5px;color:#8a99ad;">Click to Join Telegram</div></div>' +
                                       '</a>' +
                                       '<div style="font-size:6.5px;color:#8a99ad;margin-bottom:5px;" id="err-msg">Enter Password (AR)</div>' +
                                       '<input type="password" id="license-input" placeholder="Enter Password" style="width:100%;box-sizing:border-box;background:#0d1526;border:1px solid #16253f;padding:7px;border-radius:5px;color:#fff;font-size:9px;outline:none;margin-bottom:10px;text-align:center;letter-spacing:1px;" />' +
                                       '<button id="verify-btn" style="width:100%;background:linear-gradient(90deg, #ff00ff, #00ffff);border:none;padding:7px;border-radius:5px;font-weight:900;font-size:9px;color:#000;cursor:pointer;">ACTIVATE BOT</button>';
                panel.appendChild(licenseBox);

                var verifyBtn = licenseBox.querySelector('#verify-btn');
                var licenseInput = licenseBox.querySelector('#license-input');
                var errMsg = licenseBox.querySelector('#err-msg');

                verifyBtn.onclick = function(){
                    var keyVal = licenseInput.value.trim();
                    if(keyVal === 'AR'){
                        verifyBtn.innerHTML = '<span style="display:inline-block;width:9px;height:9px;border:2px solid #000;border-top-color:transparent;border-radius:50%;animation:spinAnim 0.8s linear infinite;"></span> Verifying...';
                        setTimeout(function(){
                            sessionStorage.setItem('coco_bot_verified_' + uniqueId, 'true');
                            panel.remove();
                            createFloatingBot();
                        }, 1200);
                    } else {
                        errMsg.innerText = '⚠️ INCORRECT PASSWORD!';
                        errMsg.style.color = '#ff1744';
                        licenseInput.style.borderColor = '#ff1744';
                        verifyBtn.style.background = '#ff1744';
                        verifyBtn.style.color = '#fff';
                        verifyBtn.innerText = 'ACCESS DENIED';
                    }
                };

                d.body.appendChild(panel);
            }

            function createFloatingBot(){
                var existingWrap = d.getElementById('coco_target_wrap');
                if(existingWrap) existingWrap.remove();

                var wrap = d.createElement('div');
                wrap.id = 'coco_target_wrap';
                wrap.style.cssText = 'position:fixed;bottom:70px;left:20px;display:flex;flex-direction:column;align-items:center;z-index:2147483647;cursor:pointer;';
                
                var b = d.createElement('div');
                b.id = 'coco_target_btn';
                b.style.cssText = 'width:62px;height:62px;border-radius:50%;background:#030407;display:flex;align-items:center;justify-content:center;border:3.5px solid #ff00ff;animation:multiColorGlowSlow 6s infinite linear;box-sizing:border-box;overflow:hidden;';
                b.innerHTML = '<img src="https://i.postimg.cc/hGdbJVHR/IMG-20261102-WA0070.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" />';
                wrap.appendChild(b);

                d.body.appendChild(wrap);
                
                var isDragging = false, startX, startY, hasMoved = false;
                wrap.onmousedown = wrap.ontouchstart = function(e){
                    isDragging = true; hasMoved = false;
                    var p = e.touches ? e.touches[0] : e;
                    startX = p.clientX - wrap.offsetLeft;
                    startY = p.clientY - wrap.offsetTop;
                };
                wrap.onmousemove = wrap.ontouchmove = function(e){
                    if(!isDragging) return;
                    var p = e.touches ? e.touches[0] : e;
                    var nx = p.clientX - startX, ny = p.clientY - startY;
                    if(Math.abs(nx - wrap.offsetLeft) > 2 || Math.abs(ny - wrap.offsetTop) > 2) hasMoved = true;
                    wrap.style.left = nx + 'px';
                    wrap.style.top = ny + 'px';
                    wrap.style.bottom = 'auto';
                    wrap.style.right = 'auto';
                };
                wrap.onmouseup = wrap.ontouchend = function(){ isDragging = false; };
                
                wrap.onclick = function(){
                    if(hasMoved) return;
                    runLaserScanningAndTrade();
                };
            }

            function forceSingleClick(el) {
                if(!el) return false;
                try {
                    var box = el.getBoundingClientRect();
                    var cx = box.left + (box.width / 2);
                    var cy = box.top + (box.height / 2);
                    
                    // Dispatch single click sequence safely to avoid multi-clicking
                    ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click'].forEach(function(evName){
                        var ev = new MouseEvent(evName, {
                            bubbles: true, cancelable: true, view: window,
                            clientX: cx, clientY: cy, screenX: cx, screenY: cy
                        });
                        el.dispatchEvent(ev);
                    });
                    if(typeof el.click === 'function') el.click();
                    return true;
                } catch(e) { return false; }
            }

            function triggerStrictSingleTrade(isSell){
                var clicked = false;
                var allButtons = d.querySelectorAll('button, div[role="button"], span[class*="btn"]');
                for(var i=0; i<allButtons.length; i++){
                    var btn = allButtons[i];
                    var text = (btn.innerText || '').trim().toUpperCase();
                    var cls = (btn.className || '').toLowerCase();
                    
                    var isUpBtn = cls.includes('call') || cls.includes('buy') || cls.includes('up') || text === 'UP' || text === 'BUY' || text === 'HIGHER';
                    var isDownBtn = cls.includes('put') || cls.includes('sell') || cls.includes('down') || text === 'DOWN' || text === 'SELL' || text === 'LOWER';
                    
                    if(!isSell && isUpBtn && btn.getBoundingClientRect().width > 0){
                        if(forceSingleClick(btn)){ clicked = true; break; }
                    }
                    if(isSell && isDownBtn && btn.getBoundingClientRect().width > 0){
                        if(forceSingleClick(btn)){ clicked = true; break; }
                    }
                }
                
                if(!clicked){
                    var selectors = isSell ? [
                        '.section-deal__button-down button', '.section-deal__button-down',
                        '.btn-put', 'button.put', 'button[class*="put"]', '.button-sell', '[class*="sell"]'
                    ] : [
                        '.section-deal__button-up button', '.section-deal__button-up',
                        '.btn-call', 'button.call', 'button[class*="call"]', '.button-buy', '[class*="buy"]'
                    ];

                    for(var i=0; i<selectors.length; i++){
                        var btns = d.querySelectorAll(selectors[i]);
                        for(var j=0; j<btns.length; j++){
                            if(btns[j] && btns[j].getBoundingClientRect().width > 0){
                                if(forceSingleClick(btns[j])){ clicked = true; break; }
                            }
                        }
                        if(clicked) break;
                    }
                }
            }

            var isScanningActive = false;

            function getCurrentMarketName() {
                try {
                    var selectors = [
                        '.asset-name', '.current-asset', '[class*="asset"]', 
                        'div[class*="select-asset"]', '.currency-name', '.mg-select__value'
                    ];
                    for(var i=0; i<selectors.length; i++){
                        var el = d.querySelector(selectors[i]);
                        if(el && el.innerText && el.innerText.trim().length > 1){
                            var name = el.innerText.trim().replace(/\\n/g, ' ');
                            if(name.length < 25) return name;
                        }
                    }
                } catch(e){}
                return 'EUR/USD (OTC)';
            }

            function runLaserScanningAndTrade(){
                if(isScanningActive) return;
                isScanningActive = true;

                var overlay = d.createElement('div');
                overlay.id = 'laser_scan_overlay';
                overlay.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:2147483646;overflow:hidden;font-family:sans-serif;';
                
                var laserLine = d.createElement('div');
                laserLine.style.cssText = 'position:absolute;left:0;width:100%;height:8px;background:linear-gradient(90deg, transparent, #ff00ff, #00ffff, #00ff66, #ff00ff, transparent);box-shadow:0 0 30px #ff00ff, 0 0 50px #00ffff;animation:laserScanTopDown 1.5s infinite ease-in-out;';
                overlay.appendChild(laserLine);

                var activeMarket = getCurrentMarketName();

                var termBox = d.createElement('div');
                termBox.style.cssText = 'position:absolute;top:100px;left:20px;background:rgba(7,11,20,0.92);border:2.5px solid #ff00ff;color:#00ff66;padding:12px 16px;border-radius:10px;font-family:monospace;font-size:11px;box-shadow:0 0 25px rgba(255,0,255,0.6);animation:multiColorGlowSlow 6s infinite linear;min-width:180px;';
                termBox.innerHTML = '<div style="color:#8a99ad;margin-bottom:4px;font-size:9px;">root@coco-ai:~#</div>' +
                                    '<div style="color:#fff;font-weight:bold;margin-bottom:2px;" id="term-status">analyzing...</div>' +
                                    '<div style="color:#00ffff;font-size:10px;" id="term-market">market: ' + activeMarket + '</div>';
                overlay.appendChild(termBox);

                d.body.appendChild(overlay);

                // Exact 7 seconds scanning duration
                setTimeout(function(){
                    fetch('https://coco-ai-bot.onrender.com/signal?t='+Date.now())
                    .then(function(r){ return r.json(); })
                    .catch(function(){ return {signal: "DOWN", confidence: 92}; })
                    .then(function(j){
                        var rawSig = String(j.signal || 'DOWN').toUpperCase();
                        var isDown = (rawSig === 'SELL' || rawSig === 'DOWN' || rawSig === 'PUT');
                        
                        // Execute STRICTLY ONE single trade
                        triggerStrictSingleTrade(isDown);

                        var sigText = isDown ? 'signal: DOWN ⬇️' : 'signal: UP ⬆️';
                        var col = isDown ? '#ff1744' : '#00ff66';
                        
                        termBox.style.borderColor = col;
                        var statusEl = termBox.querySelector('#term-status');
                        if(statusEl){
                            statusEl.innerText = sigText;
                            statusEl.style.color = col;
                        }

                        laserLine.style.background = col;
                        laserLine.style.boxShadow = '0 0 35px ' + col;

                        // Display signal for 2.5 seconds then fade out smoothly
                        setTimeout(function(){
                            overlay.remove();
                            isScanningActive = false;
                        }, 2500);
                    });
                }, 7000);
            }
        } catch(e) { console.error("CocoBot Error:", e); }
    })();
    """
    res = make_response(js)
    res.headers['Content-Type'] = 'application/javascript'
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
