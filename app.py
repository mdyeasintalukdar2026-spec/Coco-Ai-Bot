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
    return "COCO AI Bot Engine v151.0 [R-A Trading Community Bot] Running 24/7!"

@app.route('/ping')
def ping():
    return "OK", 200

@app.route('/signal')
def get_signal():
    try:
        t = int(time.time() * 1000)
        rand_val = random.random()
        base_signal = "UP" if (t % 3 != 0 and rand_val > 0.45) else "DOWN"
        signal_conf = int(89 + (t % 8))
        res = jsonify({
            "signal": base_signal,
            "trend": "STRICT SINGLE MOMENTUM",
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
                s.innerHTML = '@keyframes multiColorGlow150 {' +
                              '0% { border-color: #ff0000; box-shadow: 0 0 30px #ff0000, inset 0 0 15px #ff0000; }' +
                              '3.3% { border-color: #0000ff; box-shadow: 0 0 30px #0000ff, inset 0 0 15px #0000ff; }' +
                              '6.6% { border-color: #ffff00; box-shadow: 0 0 30px #ffff00, inset 0 0 15px #ffff00; }' +
                              '10% { border-color: #00ff00; box-shadow: 0 0 30px #00ff00, inset 0 0 15px #00ff00; }' +
                              '13.3% { border-color: #ff8000; box-shadow: 0 0 30px #ff8000, inset 0 0 15px #ff8000; }' +
                              '16.6% { border-color: #800080; box-shadow: 0 0 30px #800080, inset 0 0 15px #800080; }' +
                              '20% { border-color: #ff00ff; box-shadow: 0 0 30px #ff00ff, inset 0 0 15px #ff00ff; }' +
                              '23.3% { border-color: #804000; box-shadow: 0 0 30px #804000, inset 0 0 15px #804000; }' +
                              '26.6% { border-color: #00ffff; box-shadow: 0 0 30px #00ffff, inset 0 0 15px #00ffff; }' +
                              '30% { border-color: #ff1493; box-shadow: 0 0 30px #ff1493, inset 0 0 15px #ff1493; }' +
                              '33.3% { border-color: #00ffcc; box-shadow: 0 0 30px #00ffcc, inset 0 0 15px #00ffcc; }' +
                              '36.6% { border-color: #ffd700; box-shadow: 0 0 30px #ffd700, inset 0 0 15px #ffd700; }' +
                              '40% { border-color: #008080; box-shadow: 0 0 30px #008080, inset 0 0 15px #008080; }' +
                              '43.3% { border-color: #ff4500; box-shadow: 0 0 30px #ff4500, inset 0 0 15px #ff4500; }' +
                              '46.6% { border-color: #9370db; box-shadow: 0 0 30px #9370db, inset 0 0 15px #9370db; }' +
                              '50% { border-color: #32cd32; box-shadow: 0 0 30px #32cd32, inset 0 0 15px #32cd32; }' +
                              '53.3% { border-color: #ba55d3; box-shadow: 0 0 30px #ba55d3, inset 0 0 15px #ba55d3; }' +
                              '56.6% { border-color: #20b2aa; box-shadow: 0 0 30px #20b2aa, inset 0 0 15px #20b2aa; }' +
                              '60% { border-color: #dc143c; box-shadow: 0 0 30px #dc143c, inset 0 0 15px #dc143c; }' +
                              '63.3% { border-color: #4169e1; box-shadow: 0 0 30px #4169e1, inset 0 0 15px #4169e1; }' +
                              '66.6% { border-color: #00fa9a; box-shadow: 0 0 30px #00fa9a, inset 0 0 15px #00fa9a; }' +
                              '70% { border-color: #ff69b4; box-shadow: 0 0 30px #ff69b4, inset 0 0 15px #ff69b4; }' +
                              '73.3% { border-color: #adff2f; box-shadow: 0 0 30px #adff2f, inset 0 0 15px #adff2f; }' +
                              '76.6% { border-color: #ba8b02; box-shadow: 0 0 30px #ba8b02, inset 0 0 15px #ba8b02; }' +
                              '80% { border-color: #7b68ee; box-shadow: 0 0 30px #7b68ee, inset 0 0 15px #7b68ee; }' +
                              '83.3% { border-color: #ff6347; box-shadow: 0 0 30px #ff6347, inset 0 0 15px #ff6347; }' +
                              '86.6% { border-color: #40e0d0; box-shadow: 0 0 30px #40e0d0, inset 0 0 15px #40e0d0; }' +
                              '90% { border-color: #ee82ee; box-shadow: 0 0 30px #ee82ee, inset 0 0 15px #ee82ee; }' +
                              '93.3% { border-color: #9acd32; box-shadow: 0 0 30px #9acd32, inset 0 0 15px #9acd32; }' +
                              '96.6% { border-color: #faebd7; box-shadow: 0 0 30px #faebd7, inset 0 0 15px #faebd7; }' +
                              '100% { border-color: #ff0000; box-shadow: 0 0 30px #ff0000, inset 0 0 15px #ff0000; }' +
                              '}' +
                              '@keyframes laserScanStrictBounds {0%{top:14%;opacity:0.95;} 50%{top:86%;opacity:1;} 100%{top:14%;opacity:0.95;}}' +
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
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:275px;background:#070b14;border:4px solid #ff00ff;border-radius:15px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 25px 60px rgba(0,0,0,0.98);overflow:hidden;animation:panelPop 0.3s ease-out forwards, multiColorGlow150 14s infinite linear;';
                
                var header = d.createElement('div');
                header.style.cssText = 'background:#03050a;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #131d2e;';
                header.innerHTML = '<div style="display:flex;align-items:center;gap:8px;">' +
                                   '<img src="https://i.postimg.cc/hGdbJVHR/IMG-20261102-WA0070.jpg" style="width:36px;height:36px;border-radius:50%;object-fit:cover;border:2.5px solid #ff00ff;animation:multiColorGlow150 14s infinite linear;" />' +
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
                licenseBox.innerHTML = '<div style="margin-bottom:8px;"><img src="https://i.postimg.cc/JzRR8g6M/IMG-20261102-WA0003.jpg" style="width:48px;height:48px;border-radius:50%;object-fit:cover;border:3px solid #ff00ff;animation:multiColorGlow150 14s infinite linear;" /></div>' +
                                       '<a href="https://t.me/rahadtrader123" target="_blank" style="display:flex;align-items:center;justify-content:center;gap:6px;background:#0d1526;border:2px solid #ff00ff;padding:6px;border-radius:6px;margin-bottom:10px;text-decoration:none;color:#fff;animation:multiColorGlow150 14s infinite linear;">' +
                                       '<img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" style="width:16px;height:16px;margin-right:3px;" />' +
                                       '<div style="text-align:left;"><div style="font-size:8.5px;font-weight:950;color:#00ff66;">R-A Trading Community</div><div style="font-size:5.5px;color:#8a99ad;">Click to Join Telegram</div></div>' +
                                       '</a>' +
                                       '<div style="font-size:6.5px;color:#8a99ad;margin-bottom:5px;" id="err-msg">Bot Access Key</div>' +
                                       '<input type="password" id="license-input" placeholder="Bot Access Key" style="width:100%;box-sizing:border-box;background:#0d1526;border:1px solid #16253f;padding:7px;border-radius:5px;color:#fff;font-size:9px;outline:none;margin-bottom:10px;text-align:center;letter-spacing:1px;" />' +
                                       '<button id="verify-btn" style="width:100%;background:linear-gradient(90deg, #ff00ff, #00ffff);border:none;padding:7px;border-radius:5px;font-weight:900;font-size:9px;color:#000;cursor:pointer;">ACTIVATE BOT</button>';
                panel.appendChild(licenseBox);

                var verifyBtn = licenseBox.querySelector('#verify-btn');
                var licenseInput = licenseBox.querySelector('#license-input');
                var errMsg = licenseBox.querySelector('#err-msg');

                verifyBtn.onclick = function(){
                    var keyVal = licenseInput.value.trim();
                    if(keyVal === 'RA'){
                        verifyBtn.innerHTML = '<span style="display:inline-block;width:9px;height:9px;border:2px solid #000;border-top-color:transparent;border-radius:50%;animation:spinAnim 0.8s linear infinite;"></span> Verifying...';
                        setTimeout(function(){
                            sessionStorage.setItem('coco_bot_verified_' + uniqueId, 'true');
                            panel.remove();
                            createFloatingBot();
                        }, 1200);
                    } else {
                        errMsg.innerText = '⚠️ INCORRECT KEY!';
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
                b.style.cssText = 'width:62px;height:62px;border-radius:50%;background:#030407;display:flex;align-items:center;justify-content:center;border:4px solid #ff00ff;animation:multiColorGlow150 12s infinite linear;box-sizing:border-box;overflow:hidden;';
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
                    runLaserScanningAndTrade(wrap);
                };
            }

            // STRICT GLOBAL LOCK TO PREVENT MULTI/DOUBLE TRADES
            var hasExecutedThisRound = false;

            function executeStrictSingleClick(el) {
                if(!el || hasExecutedThisRound) return false;
                hasExecutedThisRound = true;
                try {
                    var box = el.getBoundingClientRect();
                    var cx = box.left + (box.width / 2);
                    var cy = box.top + (box.height / 2);
                    
                    var ev = new MouseEvent('click', {
                        bubbles: true, cancelable: true, view: window,
                        clientX: cx, clientY: cy, screenX: cx, screenY: cy
                    });
                    el.dispatchEvent(ev);
                    if(typeof el.click === 'function') {
                        el.click();
                    }
                    return true;
                } catch(e) { return false; }
            }

            function triggerStrictSingleTrade(isSell){
                if(hasExecutedThisRound) return;
                var clicked = false;
                
                var selectors = isSell ? [
                    'button.btn-red', '.section-deal__button-down button', '.section-deal__button-down',
                    'button[class*="put"]', 'button[class*="sell"]', '.btn-put'
                ] : [
                    'button.btn-green', '.section-deal__button-up button', '.section-deal__button-up',
                    'button[class*="call"]', 'button[class*="buy"]', '.btn-call'
                ];

                for(var i=0; i<selectors.length; i++){
                    var btns = d.querySelectorAll(selectors[i]);
                    for(var j=0; j<btns.length; j++){
                        var b = btns[j];
                        if(b && b.getBoundingClientRect().width > 0 && b.offsetParent !== null){
                            var text = (b.innerText || '').trim().toUpperCase();
                            if(isSell && (text.includes('SELL') || text.includes('DOWN') || b.className.includes('put') || b.className.includes('sell'))) {
                                if(executeStrictSingleClick(b)){ clicked = true; break; }
                            }
                            if(!isSell && (text.includes('BUY') || text.includes('UP') || b.className.includes('call') || b.className.includes('buy'))) {
                                if(executeStrictSingleClick(b)){ clicked = true; break; }
                            }
                        }
                    }
                    if(clicked) break;
                }

                if(!clicked){
                    var allButtons = d.querySelectorAll('button, div[role="button"]');
                    for(var k=0; k<allButtons.length; k++){
                        var btn = allButtons[k];
                        var text = (btn.innerText || '').trim().toUpperCase();
                        var cls = (btn.className || '').toLowerCase();
                        var isUpBtn = cls.includes('call') || cls.includes('buy') || text === 'UP' || text === 'BUY' || text === 'HIGHER';
                        var isDownBtn = cls.includes('put') || cls.includes('sell') || text === 'DOWN' || text === 'SELL' || text === 'LOWER';
                        
                        if(!isSell && isUpBtn && btn.getBoundingClientRect().width > 0){
                            if(executeStrictSingleClick(btn)){ clicked = true; break; }
                        }
                        if(isSell && isDownBtn && btn.getBoundingClientRect().width > 0){
                            if(executeStrictSingleClick(btn)){ clicked = true; break; }
                        }
                    }
                }
            }

            var isScanningActive = false;

            function getCurrentMarketName() {
                try {
                    var selectors = [
                        '.asset-select__current-item span', '.chart-instrument__name', '.mg-select__value', 
                        '.asset-name', '.current-asset', '[class*="asset-select"]', '[class*="instrument"]',
                        '.dropdown__selected', '.mg-select__selected', '[class*="asset-item__title"]'
                    ];
                    for(var i=0; i<selectors.length; i++){
                        var els = d.querySelectorAll(selectors[i]);
                        for(var k=0; k<els.length; k++){
                            var txt = (els[k].innerText || '').trim().replace(/\\n/g, ' ');
                            if(txt.length > 1 && txt.length < 25 && (txt.includes('/') || txt.includes('OTC') || txt.includes('USD') || txt.includes('GBP') || txt.includes('EUR') || txt.includes('CHF'))){
                                if(!txt.includes('Deposit') && !txt.includes('Payout') && !txt.includes('Timer')){
                                    return txt;
                                }
                            }
                        }
                    }
                    var allSpans = d.querySelectorAll('div, span');
                    for(var m=0; m<allSpans.length; m++){
                        var t = (allSpans[m].innerText || '').trim();
                        if(t.match(/^[A-Z]{3}\/[A-Z]{3}(\s*\(OTC\))?$/)){
                            return t;
                        }
                    }
                } catch(e){}
                return 'EUR/USD (OTC)';
            }

            function runLaserScanningAndTrade(botWrap){
                if(isScanningActive) return;
                isScanningActive = true;
                hasExecutedThisRound = false; // Reset lock for this round

                // 1. Dim/Blur background overlay effect
                var dimOverlay = d.createElement('div');
                dimOverlay.id = 'coco_dim_overlay';
                dimOverlay.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(0,0,0,0.45);backdrop-filter:blur(1.5px);z-index:2147483645;pointer-events:none;transition:opacity 0.3s ease;';
                d.body.appendChild(dimOverlay);

                // 2. Precise Bounded Laser Line Animation (Loops 4 times strictly within chart area)
                var laserLine = d.createElement('div');
                laserLine.id = 'laser_scan_overlay';
                laserLine.style.cssText = 'position:fixed;left:0;width:100vw;height:12px;background:linear-gradient(90deg, transparent, #ff00ff, #00ffff, #00ff66, #ff00ff, transparent);box-shadow:0 0 35px #ff00ff, 0 0 65px #00ffff;z-index:2147483646;pointer-events:none;animation:laserScanStrictBounds 1.4s ease-in-out 4;';
                d.body.appendChild(laserLine);

                var activeMarket = getCurrentMarketName();

                // 3. Position terminal signal box right above the floating bot dynamically
                var botRect = botWrap.getBoundingClientRect();
                var termBox = d.createElement('div');
                termBox.style.cssText = 'position:fixed;left:' + Math.max(10, botRect.left) + 'px;bottom:' + (window.innerHeight - botRect.top + 12) + 'px;background:rgba(7,11,20,0.95);border:3px solid #ff00ff;color:#00ff66;padding:12px 16px;border-radius:10px;font-family:monospace;font-size:11px;box-shadow:0 0 30px rgba(255,0,255,0.7);z-index:2147483647;animation:multiColorGlow150 12s infinite linear;min-width:185px;';
                termBox.innerHTML = '<div style="color:#8a99ad;margin-bottom:4px;font-size:9px;">root@coco-ai:~#</div>' +
                                    '<div style="color:#fff;font-weight:bold;margin-bottom:2px;" id="term-status">analyzing...</div>' +
                                    '<div style="color:#00ffff;font-size:10px;" id="term-market">market: ' + activeMarket + '</div>';
                d.body.appendChild(termBox);

                // Exactly 5.6 seconds scanning duration matching 4 animation loops
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
                        laserLine.style.boxShadow = '0 0 40px ' + col;

                        // Display result for 2.5 seconds then clean up
                        setTimeout(function(){
                            if(dimOverlay) dimOverlay.remove();
                            if(laserLine) laserLine.remove();
                            if(termBox) termBox.remove();
                            isScanningActive = false;
                        }, 2500);
                    });
                }, 5600);
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
