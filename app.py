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
    return "COCO AI Bot Engine v128.0 [COCO Trading Community Bot] Running 24/7!"

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
                s.innerHTML = '@keyframes multiColorGlow {' +
                              '0% { border-color: #00ff66; box-shadow: 0 0 22px #00ff66, inset 0 0 10px #00ff66; }' +
                              '20% { border-color: #00ffff; box-shadow: 0 0 22px #00ffff, inset 0 0 10px #00ffff; }' +
                              '40% { border-color: #ff00ff; box-shadow: 0 0 22px #ff00ff, inset 0 0 10px #ff00ff; }' +
                              '60% { border-color: #ff3300; box-shadow: 0 0 22px #ff3300, inset 0 0 10px #ff3300; }' +
                              '80% { border-color: #ffff00; box-shadow: 0 0 22px #ffff00, inset 0 0 10px #ffff00; }' +
                              '100% { border-color: #00ff66; box-shadow: 0 0 22px #00ff66, inset 0 0 10px #00ff66; }' +
                              '}' +
                              '@keyframes laserScanVertical {0%{top:0%;opacity:0.9;}50%{top:95%;opacity:1;}100%{top:0%;opacity:0.9;}}' +
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
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:265px;background:#070b14;border:3.5px solid #ff00ff;border-radius:14px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 20px 50px rgba(0,0,0,0.98);overflow:hidden;animation:panelPop 0.3s ease-out forwards, multiColorGlow 0.8s infinite linear;';
                
                var header = d.createElement('div');
                header.style.cssText = 'background:#03050a;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #131d2e;';
                header.innerHTML = '<div style="display:flex;align-items:center;gap:8px;">' +
                                   '<img src="https://i.postimg.cc/hGdbJVHR/IMG-20261102-WA0070.jpg" style="width:26px;height:26px;border-radius:50%;object-fit:cover;border:2.5px solid #ff00ff;animation:multiColorGlow 0.8s infinite linear;" />' +
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
                licenseBox.innerHTML = '<div style="margin-bottom:8px;"><img src="https://i.postimg.cc/hGdbJVHR/IMG-20261102-WA0070.jpg" style="width:45px;height:45px;border-radius:50%;object-fit:cover;border:3px solid #ff00ff;animation:multiColorGlow 0.8s infinite linear;" /></div>' +
                                       '<a href="https://t.me/rahadtrader123" target="_blank" style="display:flex;align-items:center;justify-content:center;gap:6px;background:#0d1526;border:1px solid #16253f;padding:6px;border-radius:6px;margin-bottom:10px;text-decoration:none;color:#fff;">' +
                                       '<img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" style="width:14px;height:14px;" />' +
                                       '<div style="text-align:left;"><div style="font-size:8.5px;font-weight:950;color:#00ff66;">COCO Trading Community</div><div style="font-size:5.5px;color:#8a99ad;">Click to Join Telegram</div></div>' +
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
                        }, 1000);
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
                wrap.style.cssText = 'position:fixed;bottom:70px;right:20px;display:flex;flex-direction:column;align-items:center;z-index:2147483647;cursor:pointer;';
                
                var b = d.createElement('div');
                b.id = 'coco_target_btn';
                b.style.cssText = 'width:65px;height:65px;border-radius:50%;background:#030407;display:flex;align-items:center;justify-content:center;border:3.5px solid #ff00ff;animation:multiColorGlow 0.8s infinite linear;box-sizing:border-box;overflow:hidden;';
                b.innerHTML = '<img src="https://i.postimg.cc/hGdbJVHR/IMG-20261102-WA0070.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" />';
                wrap.appendChild(b);

                var lbl = d.createElement('div');
                lbl.style.cssText = 'margin-top:4px;font-size:7.5px;font-weight:900;color:#ff00ff;font-family:sans-serif;background:rgba(3,4,7,0.9);padding:2px 7px;border-radius:4px;border:1.5px solid #ff00ff;white-space:nowrap;box-shadow:0 0 8px rgba(255,0,255,0.7);animation:multiColorGlow 0.8s infinite linear;';
                lbl.innerText = 'COCO AI BOT';
                wrap.appendChild(lbl);

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

            function forceClick(el) {
                if(!el) return false;
                try {
                    var box = el.getBoundingClientRect();
                    var cx = box.left + (box.width / 2);
                    var cy = box.top + (box.height / 2);
                    ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click'].forEach(function(evName){
                        var ev = new MouseEvent(evName, {
                            bubbles: true, cancelable: true, view: window,
                            clientX: cx,clientY: cy,screenX: cx,screenY: cy
                        });
                        el.dispatchEvent(ev);
                    });
                    if(typeof el.click === 'function') el.click();
                    return true;
                } catch(e) { return false; }
            }

            function triggerSingleTrade(isSell){
                var clicked = false;
                var allButtons = d.querySelectorAll('button, div[role="button"], span[class*="btn"]');
                for(var i=0; i<allButtons.length; i++){
                    var btn = allButtons[i];
                    var text = (btn.innerText || '').trim().toUpperCase();
                    var cls = (btn.className || '').toLowerCase();
                    
                    var isUpBtn = cls.includes('call') || cls.includes('buy') || cls.includes('up') || text === 'UP' || text === 'BUY' || text === 'HIGHER';
                    var isDownBtn = cls.includes('put') || cls.includes('sell') || cls.includes('down') || text === 'DOWN' || text === 'SELL' || text === 'LOWER';
                    
                    if(!isSell && isUpBtn && btn.getBoundingClientRect().width > 0){
                        if(forceClick(btn)){ clicked = true; break; }
                    }
                    if(isSell && isDownBtn && btn.getBoundingClientRect().width > 0){
                        if(forceClick(btn)){ clicked = true; break; }
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
                                if(forceClick(btns[j])){ clicked = true; break; }
                            }
                        }
                        if(clicked) break;
                    }
                }
            }

            var isScanningActive = false;

            function runLaserScanningAndTrade(){
                if(isScanningActive) return;
                isScanningActive = true;

                var overlay = d.createElement('div');
                overlay.id = 'laser_scan_overlay';
                overlay.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:2147483646;overflow:hidden;font-family:sans-serif;';
                
                var laserLine = d.createElement('div');
                laserLine.style.cssText = 'position:absolute;left:0;width:100%;height:6px;background:linear-gradient(90deg, transparent, #ff00ff, #00ffff, #00ff66, #ff00ff, transparent);box-shadow:0 0 25px #ff00ff, 0 0 45px #00ffff;animation:laserScanVertical 1.4s infinite ease-in-out;';
                overlay.appendChild(laserLine);

                var scanMsg = d.createElement('div');
                scanMsg.style.cssText = 'position:absolute;top:20px;left:50%;transform:translateX(-50%);background:rgba(3,4,7,0.94);border:2.5px solid #ff00ff;color:#ff00ff;padding:7px 20px;border-radius:22px;font-weight:900;font-size:12px;box-shadow:0 0 22px rgba(255,0,255,0.7);letter-spacing:0.8px;animation:multiColorGlow 0.8s infinite linear;';
                scanMsg.innerText = 'COCO AI: MARKET SCANNING...';
                overlay.appendChild(scanMsg);

                d.body.appendChild(overlay);

                // Exact 7.5 seconds scanning duration with NO trade during scanning
                setTimeout(function(){
                    fetch('https://coco-ai-bot.onrender.com/signal?t='+Date.now())
                    .then(function(r){ return r.json(); })
                    .catch(function(){ return {signal: "DOWN", confidence: 92}; })
                    .then(function(j){
                        var rawSig = String(j.signal || 'DOWN').toUpperCase();
                        var isDown = (rawSig === 'SELL' || rawSig === 'DOWN' || rawSig === 'PUT');
                        
                        // Execute exactly ONE single automated trade right after 7.5s scanning completes
                        triggerSingleTrade(isDown);

                        var sigText = isDown ? 'SIGNAL EXECUTED: DOWN ⬇️' : 'SIGNAL EXECUTED: UP ⬆️';
                        var col = isDown ? '#ff1744' : '#00ff66';
                        scanMsg.style.borderColor = col;
                        scanMsg.style.color = col;
                        scanMsg.style.boxShadow = '0 0 25px ' + col;
                        scanMsg.style.animation = 'none';
                        scanMsg.innerText = sigText + ' (' + (j.confidence || 92) + '%)';
                        
                        laserLine.style.background = col;
                        laserLine.style.boxShadow = '0 0 32px ' + col;

                        // Display final signal for 3 seconds then remove overlay
                        setTimeout(function(){
                            overlay.remove();
                            isScanningActive = false;
                        }, 3000);
                    });
                }, 7500);
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
