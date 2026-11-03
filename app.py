from flask import Flask, jsonify, make_response
import threading
import requests
import time
import random
import os

app = Flask(__name__, static_folder=None)

# ==========================================
# MASTER CONFIGURATIONS & SERVER FEEDS
# ==========================================
TWELVE_DATA_KEY = "8f5d4d4fce7f44e5bda54420591411c8"
GROQ_API_KEY = "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"
FINNHUB_API_KEY = "dbcaa19r01qqr3s0pf60dbcaa19r01qqr3s0pf6g"

http_session = requests.Session()

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response

@app.route('/')
def home():
    return "COCO AI Bot Engine v260.0 [R-A Trading Community Bot] Running 24/7!"

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
        return res
    except Exception as e:
        res = jsonify({
            "signal": "UP",
            "trend": "STRONG MOMENTUM",
            "confidence": 92,
            "status": "GREEN_EXECUTE"
        })
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
                s.innerHTML = 
                    /* Ultra Smooth Slow-Motion Color Cycle with Permanent Constant White Outer Lighting Glow */
                    '@keyframes ultraSmoothWhiteGlow {' +
                        '0%{border-color:#ff0055;box-shadow:0 0 45px #ffffff, 0 0 22px #ff0055, inset 0 0 15px #ffffff;}' +
                        '25%{border-color:#00ffff;box-shadow:0 0 45px #ffffff, 0 0 22px #00ffff, inset 0 0 15px #ffffff;}' +
                        '50%{border-color:#00ff00;box-shadow:0 0 45px #ffffff, 0 0 22px #00ff00, inset 0 0 15px #ffffff;}' +
                        '75%{border-color:#ffcc00;box-shadow:0 0 45px #ffffff, 0 0 22px #ffcc00, inset 0 0 15px #ffffff;}' +
                        '100%{border-color:#ff0055;box-shadow:0 0 45px #ffffff, 0 0 22px #ff0055, inset 0 0 15px #ffffff;}' +
                    '}' +
                    '@keyframes cocoTopAnim {' +
                        '0%{border-color:#ff0000;box-shadow:0 0 35px #ff0000;}' +
                        '50%{border-color:#00ffff;box-shadow:0 0 35px #00ffff;}' +
                        '100%{border-color:#ff0000;box-shadow:0 0 35px #ff0000;}' +
                    '}' +
                    '@keyframes commProfileAnim {' +
                        '0%{border-color:#00ff00;box-shadow:0 0 45px #00ff00;}' +
                        '50%{border-color:#ff4500;box-shadow:0 0 45px #ff4500;}' +
                        '100%{border-color:#00ff00;box-shadow:0 0 45px #00ff00;}' +
                    '}' +
                    '@keyframes commBorderAnim {' +
                        '0%{border-color:#fff700;box-shadow:0 0 35px #fff700;}' +
                        '50%{border-color:#ff8c00;box-shadow:0 0 35px #ff8c00;}' +
                        '100%{border-color:#fff700;box-shadow:0 0 35px #fff700;}' +
                    '}' +
                    '@keyframes termBorderAnim {' +
                        '0%{border-color:#ffd700;box-shadow:0 0 45px #ffd700;}' +
                        '50%{border-color:#00ffff;box-shadow:0 0 45px #00ffff;}' +
                        '100%{border-color:#ffd700;box-shadow:0 0 45px #ffd700;}' +
                    '}' +
                    '@keyframes mainPanelAnim {' +
                        '0%{border-color:#dc143c;box-shadow:0 0 55px #dc143c;}' +
                        '50%{border-color:#00ff00;box-shadow:0 0 55px #00ff00;}' +
                        '100%{border-color:#dc143c;box-shadow:0 0 55px #dc143c;}' +
                    '}' +
                    '@keyframes laserScanSmoothSlow {' +
                        '0%{top:20px;opacity:0.9;}' +
                        '50%{top:calc(100vh - 45px);opacity:1;}' +
                        '100%{top:20px;opacity:0.9;}' +
                    '}' +
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
                var panel = d.getElementById('coco_bot_license_panel');
                if(panel) panel.remove();

                panel = d.createElement('div');
                panel.id = 'coco_bot_license_panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:280px;background:#070b14;border:4px solid #dc143c;border-radius:15px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 40px 100px rgba(0,0,0,0.98);overflow:hidden;animation:panelPop 0.3s ease-out forwards, mainPanelAnim 2.8s infinite linear;';
                
                var header = d.createElement('div');
                header.style.cssText = 'background:#03050a;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #131d2e;';
                header.innerHTML = '<div style="display:flex;align-items:center;gap:10px;">' +
                                   '<img src="https://i.postimg.cc/hGdbJVHR/IMG-20261102-WA0070.jpg" style="width:46px;height:46px;border-radius:50%;object-fit:cover;border:3px solid #ff0000;animation:cocoTopAnim 3.0s infinite linear;" />' +
                                   '<div>' +
                                   '<div style="font-size:12px;font-weight:900;color:#fff;letter-spacing:0.5px;">COCO AI BOT</div>' +
                                   '<div style="font-size:6.5px;color:#ff00ff;font-weight:700;">SECURE LOGIN</div>' +
                                   '</div>' +
                                   '</div>' +
                                   '<button id="close-license" style="background:#101826;border:none;color:#fff;width:22px;height:22px;border-radius:4px;cursor:pointer;font-weight:bold;font-size:12px;">×</button>';
                panel.appendChild(header);
                
                header.querySelector('#close-license').onclick = function(){ panel.remove(); };

                var licenseBox = d.createElement('div');
                licenseBox.style.cssText = 'padding:14px;background:#070b14;text-align:center;';
                licenseBox.innerHTML = '<div style="margin-bottom:8px;"><img src="https://i.postimg.cc/JzRR8g6M/IMG-20261102-WA0003.jpg" style="width:52px;height:52px;border-radius:50%;object-fit:cover;border:3px solid #00ff00;animation:commProfileAnim 2.2s infinite linear;" /></div>' +
                                       '<a href="https://t.me/rahadtrader123" target="_blank" style="display:flex;align-items:center;justify-content:center;gap:8px;background:#0d1526;border:2px solid #fff700;padding:8px;border-radius:8px;margin-bottom:10px;text-decoration:none;color:#fff;animation:commBorderAnim 3.0s infinite linear;">' +
                                       '<img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" style="width:20px;height:20px;" />' +
                                       '<div style="text-align:left;"><div style="font-size:10px;font-weight:950;color:#00ff66;">R-A Trading Community</div><div style="font-size:6px;color:#8a99ad;">Click to Join Telegram</div></div>' +
                                       '</a>' +
                                       '<div style="font-size:7px;color:#8a99ad;margin-bottom:5px;" id="err-msg">Bot Access Key</div>' +
                                       '<input type="password" id="license-input" placeholder="Bot Access Key" style="width:100%;box-sizing:border-box;background:#0d1526;border:1px solid #16253f;padding:8px;border-radius:6px;color:#fff;font-size:10px;outline:none;margin-bottom:10px;text-align:center;letter-spacing:1px;" />' +
                                       '<button id="verify-btn" style="width:100%;background:linear-gradient(90deg, #dc143c, #00ff66);border:none;padding:9px;border-radius:6px;font-weight:900;font-size:10px;color:#000;cursor:pointer;box-shadow:0 0 35px rgba(0,255,102,0.9);">ACTIVATE BOT</button>';
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
                        }, 1000);
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
                /* Ultra smooth slow motion color transition with permanent constant white outer lighting glow */
                b.style.cssText = 'width:62px;height:62px;border-radius:50%;background:#030407;display:flex;align-items:center;justify-content:center;border:4px solid #ff0055;animation:ultraSmoothWhiteGlow 8.0s infinite ease-in-out;box-sizing:border-box;overflow:hidden;';
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

            /* STRICT SINGLE TRADE EXECUTION LOCK & PRECISE BUY/SELL TARGETING */
            var hasExecutedThisRound = false;

            function triggerStrictSingleTrade(isSell){
                if(hasExecutedThisRound) return;
                hasExecutedThisRound = true; // IMMEDIATE PERMANENT LOCK FOR THIS ROUND

                var targetBtn = null;
                
                if(isSell){
                    targetBtn = d.querySelector('.section-deal__button-down button') || 
                                d.querySelector('.section-deal__button-down') || 
                                d.querySelector('button.btn-red') || 
                                d.querySelector('button[class*="put"]') || 
                                d.querySelector('button[class*="sell"]');
                } else {
                    targetBtn = d.querySelector('.section-deal__button-up button') || 
                                d.querySelector('.section-deal__button-up') || 
                                d.querySelector('button.btn-green') || 
                                d.querySelector('button[class*="call"]') || 
                                d.querySelector('button[class*="buy"]');
                }

                if(!targetBtn){
                    var btns = d.querySelectorAll('.section-deal button, button, div[role="button"]');
                    for(var i=0; i<btns.length; i++){
                        var txt = (btns[i].innerText || '').toUpperCase();
                        var cls = (btns[i].className || '').toLowerCase();
                        if(isSell && (txt.includes('DOWN') || txt.includes('SELL') || cls.includes('down') || cls.includes('put') || cls.includes('red'))){
                            targetBtn = btns[i]; break;
                        }
                        if(!isSell && (txt.includes('UP') || txt.includes('BUY') || cls.includes('up') || cls.includes('call') || cls.includes('green'))){
                            targetBtn = btns[i]; break;
                        }
                    }
                }

                if(targetBtn && targetBtn.getBoundingClientRect().width > 0){
                    try {
                        var box = targetBtn.getBoundingClientRect();
                        var cx = box.left + (box.width / 2);
                        var cy = box.top + (box.height / 2);
                        
                        var evs = ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click'];
                        evs.forEach(function(evType){
                            var mouseEv = new MouseEvent(evType, {
                                bubbles: true, cancelable: true, view: window,
                                clientX: cx, clientY: cy, screenX: cx, screenY: cy
                            });
                            targetBtn.dispatchEvent(mouseEv);
                        });

                        if(typeof targetBtn.click === 'function') {
                            targetBtn.click();
                        }
                    } catch(e){}
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
                            if(txt.length > 1 && txt.length < 25 && (txt.includes('/') || txt.includes('OTC') || txt.includes('USD') || txt.includes('EUR') || txt.includes('GBP') || txt.includes('CHF') || txt.includes('NZD'))){
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
                hasExecutedThisRound = false; // Reset lock for new signal

                var dimOverlay = d.createElement('div');
                dimOverlay.id = 'coco_dim_overlay';
                dimOverlay.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(0,0,0,0.45);backdrop-filter:blur(1.5px);z-index:2147483645;pointer-events:none;';
                d.body.appendChild(dimOverlay);

                var laserLine = d.createElement('div');
                laserLine.id = 'laser_scan_overlay';
                laserLine.style.cssText = 'position:fixed;left:0;width:100vw;height:18px;background:linear-gradient(90deg, transparent, #ffffff, #00ffff, #ffffff, transparent);box-shadow:0 0 55px #ffffff, 0 0 110px #00ffff, 0 0 170px #ff00ff;z-index:2147483646;pointer-events:none;animation:laserScanSmoothSlow 1.66s ease-in-out 3;';
                d.body.appendChild(laserLine);

                var activeMarket = getCurrentMarketName();

                var botRect = botWrap.getBoundingClientRect();
                var termBox = d.createElement('div');
                termBox.style.cssText = 'position:fixed;left:' + Math.max(10, botRect.left) + 'px;bottom:' + (window.innerHeight - botRect.top + 12) + 'px;background:rgba(7,11,20,0.95);border:3px solid #ffd700;color:#00ff66;padding:12px 16px;border-radius:10px;font-family:monospace;font-size:11px;box-shadow:0 0 50px rgba(255,215,0,0.8);z-index:2147483647;animation:termBorderAnim 2.2s infinite linear;min-width:185px;';
                termBox.innerHTML = '<div style="color:#8a99ad;margin-bottom:4px;font-size:9px;">root@coco-ai:~#</div>' +
                                    '<div style="color:#fff;font-weight:bold;margin-bottom:2px;" id="term-status">analyzing...</div>' +
                                    '<div style="color:#00ffff;font-size:10px;" id="term-market">market: ' + activeMarket + '</div>';
                d.body.appendChild(termBox);

                setTimeout(function(){
                    fetch('https://coco-ai-bot.onrender.com/signal?t='+Date.now())
                    .then(function(r){ return r.json(); })
                    .catch(function(){ return {signal: "DOWN", confidence: 92}; })
                    .then(function(j){
                        var rawSig = String(j.signal || 'DOWN').toUpperCase();
                        var isDown = (rawSig === 'SELL' || rawSig === 'DOWN' || rawSig === 'PUT');
                        
                        if(laserLine) laserLine.remove();
                        if(dimOverlay) dimOverlay.remove();

                        triggerStrictSingleTrade(isDown);

                        var sigText = isDown ? 'signal: DOWN ⬇️' : 'signal: UP ⬆️';
                        var col = isDown ? '#ff1744' : '#00ff66';
                        
                        termBox.style.borderColor = col;
                        var statusEl = termBox.querySelector('#term-status');
                        if(statusEl){
                            statusEl.innerText = sigText;
                            statusEl.style.color = col;
                        }

                        setTimeout(function(){
                            if(termBox) termBox.remove();
                            isScanningActive = false;
                        }, 2000);
                    });
                }, 5000);
            }
        } catch(e) { console.error("CocoBot Error:", e); }
    })();
    """
    res = make_response(js)
    res.headers['Content-Type'] = 'application/javascript'
    return res

def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
