# SKILL LAB PRACTICAL HACKATHON
**Final Project README**
> Project Weight: 100% | Team Size: 2 students | Project Duration: 16 hours | Total Time Available: 32 effort-hours per team | Project Type: Playful, interactive, technology-based experience

---

## Before you begin
> Repository forked and renamed as: **SKILLLAB_PROR-2026-EdgeDetectors**

---

## How to use this README
This file is the team's working project document, updated throughout the build period to show idea, planning, design decisions, technical process, build progress, testing, failures, changes, and final outcome.

---

## 1. Team Identity

### 1.1 Studio / Group Name
**Project²**

### 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| Mrugendra Vasmatkar | Electronics / Coding / App | Documentation | Documentation, Gift of Gab |
| Jyoti Bagate | Electronics / Fabrication | Coding | Material Handling, Hardware |

### 1.3 Project Title
**"Project Project"**
*(because Project-or)*

### 1.4 One-Line Pitch
A projected, fully customizable time portal where engineering education is done through a PUBG-style battlefield — from the comfort of our home.

### 1.5 Expanded Project Idea
"Project Project" is an interactive physical-digital experience that combines a real RC car with a projector-based game environment. The car moves on a flat surface while a camera overhead tracks its position using ArUco markers. A projector throws a live game world — obstacles, targets, zones — onto that same surface. The car physically drives through the projected game, and the system detects collisions, scores points, and updates the world in real time.

The technologies involved span computer vision (OpenCV, ArUco marker tracking), embedded systems (Raspberry Pi, motor driver, DC motors), projection mapping, and Python-based game logic (PyGame). The result is an experience that feels like playing a video game except your controller is a real car driving through a real-world projection — making engineering concepts tangible, physical, and genuinely fun.

---

## 2. Inspiration

### 2.1 References

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| Video | https://www.instagram.com/reel/DW4CT7WCDry/?igsh=cXg3dzAxYmdncDBo | How projection mapping can be used to create interactive digital + physical experiences |
| Game | PUBG / top-down shooter games | The battlefield visual language — zones, obstacles, movement under pressure |

### 2.2 Original Twist
Most projection mapping projects are passive — you watch them. Ours is active: you control a real physical object that interacts with the projection in real time. The camera-tracked car means the digital world *responds* to where you physically are, not where a joystick says you are. The PUBG battlefield framing also makes it immediately legible to students — they already know the genre, so the learning experience starts with zero friction.

---

## 3. Project Intent

### 3.1 User Journey
Riya walks up to the table. She sees a flat white surface with a glowing top-down map projected onto it — a PUBG-style battlefield with walls, zones, and a blinking target marker. A small car sits at the start position.

She picks up her phone, opens the controller web page, and taps Forward. The car hums and rolls into the battlefield. The projected walls stay fixed — she has to steer around them. She taps Left, then Forward again. The car clips a wall. The projector flashes red around the obstacle and a buzzer sound plays — collision detected.

She tries again, more carefully this time. She threads the car through a corridor, reaches the glowing target zone, and the projector explodes in a green burst — level complete. A new map loads instantly. The experience lasts 90 seconds and Riya has just physically navigated coordinate systems, learned about sensors, and experienced real-time feedback loops — without reading a single slide.

---

## 4. Definition of Success

### 4.1 Definition of "Usable"
The project is usable when: a person who has never seen it before can pick up the phone controller, drive the car around the projected surface, and clearly understand when they have hit an obstacle or reached a target — without any explanation from the team.

### 4.2 Minimum Usable Version
- Car moves in all four directions via phone/web controller
- Camera tracks car position reliably using ArUco markers
- Projector displays at least one static map with obstacles and a target zone
- System detects when car reaches target zone and gives clear visual feedback

### 4.3 Stretch Features
- Multiple map levels that auto-load on completion
- Score counter and timer projected live onto the surface
- Collision sound effects
- Moving obstacles (projected)
- Two-car multiplayer mode
- Difficulty settings (faster car, tighter corridors)

---

## 5. System Overview

### 5.1 Project Type
- ✅ Electronics-based
- ✅ Mechanical
- ✅ Sensor-based
- ✅ App-connected
- ✅ Motorized
- ✅ Light-based
- ✅ Screen/UI-based
- ✅ Fabricated structure
- ✅ Game logic based

### 5.2 High-Level System Description
**Input:** Phone sends movement commands (Forward / Back / Left / Right) via HTTP to the Raspberry Pi over WiFi. A webcam mounted above the surface continuously captures the play area.

**Processing:** OpenCV on the laptop/Pi detects the ArUco marker on top of the car and computes its exact position and orientation on the surface. PyGame game logic checks this position against obstacle and target zone coordinates on the current map.

**Output:** The projector displays the live game map on the surface, updating feedback (red flash on collision, green burst on goal) in real time. The Raspberry Pi sends PWM signals to the L298N motor driver to spin the DC motors.

**Physical structure:** A laser-cut chassis carries the Raspberry Pi, motor driver, and battery pack. Two BO motors drive the wheels. An ArUco marker is mounted on top of the car for camera tracking. The play surface is white for good projection contrast.

**App interaction:** A lightweight web server runs on the Pi. The player's phone opens the IP address in a browser and gets a simple directional control UI.

### 5.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| Phone web controller | Input | Sends direction commands via HTTP |
| Webcam (overhead) | Input | Captures car position via ArUco marker |
| Raspberry Pi | Processing | Runs web server, motor control, game logic |
| OpenCV / PyGame | Processing | Tracks position, checks collisions, updates game state |
| L298N Motor Driver | Output | Drives DC motors based on Pi GPIO signals |
| BO DC Motors | Output | Move the car in four directions |
| Projector | Output | Displays game map, obstacles, feedback visuals on surface |

---

## 6. System Design, Sketches and Visual Planning

### 6.1 Concept Architecture / Sketch
*[Upload early concept sketch here]*

### 6.2 Labeled Build Sketch / Flow Diagram
*[Upload labeled diagram here — show: car chassis, Pi placement, camera mount, projector angle, surface, phone controller]*

### 6.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | 16 cm |
| Width | 16 cm |
| Height | 8 cm |
| Estimated weight | 400 g |

---

## 7. Electronics Planning

### 7.1 Electronics Used

| Component | Quantity | Purpose |
|---|---|---|
| Raspberry Pi | 1 | Main controller — runs web server, game logic, motor control |
| L298N Motor Driver | 1 | Controls direction and speed of both DC motors |
| BO DC Motors | 2 | Drive the wheels for movement |
| Buck Converter | 1 | Steps down battery voltage to stable 5V for Pi |
| Li-Ion Battery Pack | 1 | Portable power source for entire system |
| Projector | 1 | Displays the game map and feedback onto the surface |
| Webcam | 1 | Tracks car position overhead using ArUco markers |

### 7.2 Wiring Plan
The Raspberry Pi connects to the L298N motor driver using four GPIO pins (18, 19, 22, 23) for direction control (IN1, IN2, IN3, IN4), and two PWM-capable pins (25, 26) for speed control (ENA, ENB). The motor driver output terminals connect to the two BO motors. The motor driver is powered directly from the Li-Ion battery pack (7.4V nominal). The buck converter steps the battery voltage down to 5V to safely power the Raspberry Pi. All components share a common ground. The projector and webcam connect to the laptop (or Pi via USB), which handles tracking and game rendering separately.

### 7.3 Circuit Diagram
*[Upload circuit diagram here]*

### 7.4 Power Plan

| Question | Response |
|---|---|
| Power source | Li-Ion battery pack (2S, ~7.4V) |
| Voltage required | 7.4V for motors via L298N; 5V for Raspberry Pi via buck converter |
| Current concerns | Motors draw high current under load — may cause voltage sag affecting Pi stability. Decoupling capacitors added across motor terminals. |
| Safety concerns | Avoid over-discharging Li-Ion cells. Secure all wiring to prevent shorts. Buck converter output verified before connecting Pi. |

---

## 8. Software Planning

### 8.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| Python 3 | Main programming language on Raspberry Pi |
| OpenCV | Camera capture, ArUco marker detection, position tracking |
| PyGame | Game logic, map rendering, collision detection, projection output |
| Flask (Python) | Lightweight web server for phone controller UI |
| RPi.GPIO | GPIO pin control for motor driver signals |

### 8.2 Software Logic / Algorithm

**Startup:** Pi initializes GPIO pins for motor control, starts the Flask web server, opens the webcam feed, and loads the first game map into PyGame. Projector output window is set to fullscreen on the projector display.

**Input handling:** Flask receives HTTP GET requests from the phone (/forward, /back, /left, /right, /stop) and translates them into motor PWM commands via GPIO.

**Sensor reading:** OpenCV captures frames from the overhead webcam continuously. Each frame is processed to detect the ArUco marker on the car — giving X, Y position and rotation angle in the surface coordinate system.

**Decision logic:** PyGame maps the detected car position onto the game map grid. Each frame it checks whether the car's bounding box overlaps with any obstacle zone or the target zone. If an obstacle is hit → trigger collision feedback. If target is reached → load next map.

**Output behavior:** PyGame renders the game map (walls, target, score, timer) to the projector window in real time. Collision feedback = red flash overlay for 0.5s. Goal feedback = green burst + level complete screen.

**Communication logic:** Phone → HTTP request → Flask on Pi → GPIO → Motor driver → Motors. Webcam → OpenCV → position data → PyGame game logic → projector output.

**Reset behavior:** Motors stop if no command received within 500ms timeout. Game resets to start position when a level is completed or player presses reset on the web UI.

### 8.3 Code Flowchart
```
START
  │
  ├── Initialize GPIO (motor pins)
  ├── Start Flask web server
  ├── Open webcam
  └── Load Game Map 1
        │
        ▼
  MAIN LOOP
  │
  ├── [Thread 1] Flask listens for HTTP commands
  │       └── /forward /back /left /right /stop
  │               └── Set motor PWM via GPIO
  │
  ├── [Thread 2] OpenCV reads webcam frame
  │       └── Detect ArUco marker
  │               └── Extract (X, Y, angle)
  │
  └── [Thread 3] PyGame game logic
          ├── Map car position to game grid
          ├── Check collision with obstacles
          │       └── YES → Red flash, play sound
          ├── Check if target zone reached
          │       └── YES → Green burst, load next map
          └── Render updated map to projector
                │
                └── REPEAT LOOP
```

---

## 9. Bill of Materials

### 9.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---|---|---|---|---|---|
| Raspberry Pi | 1 | Yes | No | ₹0 | Raspberry Pi 4 / 3B+ | Main controller with WiFi built in |
| L298N Motor Driver | 1 | Yes | No | ₹0 | L298N dual H-bridge | Bidirectional control + PWM speed |
| BO DC Motors + Wheels | 2 | No | Yes | ₹150 | BO motor + 6cm wheels | High torque, lightweight |
| Buck Converter | 1 | No | Yes | ₹75 | 5V output, 3A | Stable regulated power for Pi |
| Li-Ion Battery Pack | 1 | No | Yes | ₹200 | 2S 18650 pack | Portable, rechargeable |
| ArUco Marker (printed) | 1 | No | No | ₹0 | Printed on paper | Camera tracking target |
| White play surface | 1 | No | No | ₹0 | A3 white sheet / board | Good projection contrast |

### 9.2 Material Justification
BO motors were chosen over servos or stepper motors because the system needs continuous rotation for free movement — not precise angular steps. Since the camera handles position tracking externally, the motor only needs to spin, not count steps. The L298N allows bidirectional PWM control from the Pi's GPIO pins without additional circuitry. The buck converter ensures the Pi receives clean 5V even as motor load fluctuates the battery voltage.

### 9.3 Items Purchased

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| BO Motors + Wheels | Drive system for car | robu.in | 15th April | Received |
| Buck Converter | Stable power for Pi | Local store | Before testing | Received |
| Li-Ion Batteries | Portable power | Local store | Before testing | Received |

### 9.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---|
| Electronics | ₹400 |
| Mechanical parts | ₹200 |
| Fabrication materials | ₹0 (available on campus) |
| Purchased extras | ₹0 |
| Contingency | ₹300 |
| **Total** | **₹900** |

### 9.5 Budget Reflection
The total is comfortably within range. If cost needed cutting, the buck converter could be replaced with a 5V USB power bank (already regulated), saving ₹75. The Li-Ion pack could be substituted with a power bank if motor load is kept low. The projector is borrowed from campus — purchasing one would be the largest cost addition, so that remains borrowed.

---

## 10. Planning the Work

### 10.1 Team Working Agreement
Tasks are divided by strength — Mrugendra owns software (Flask server, OpenCV tracking, PyGame logic) and documentation. Jyoti owns hardware (chassis fabrication, motor wiring, electronics assembly). Decisions are made together by quick verbal agreement — if stuck for more than 15 minutes, we pivot or simplify rather than block. Progress is checked at the end of every 2-hour block against the milestone list. If a task is delayed, the other member helps unblock it immediately — nothing waits overnight. Documentation is updated in real time by Mrugendra as features are built and tested.

### 10.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---|---|---|---|
| T1 | Finalize concept and system design | Both | 2 | Hour 2 | None | Done |
| T2 | Chassis fabrication (laser cut + assemble) | Jyoti | 3 | Hour 5 | T1 | Done |
| T3 | Motor wiring + GPIO test | Jyoti | 2 | Hour 6 | T2 | Done |
| T4 | Flask web server + phone controller UI | Mrugendra | 2 | Hour 6 | T1 | Done |
| T5 | OpenCV ArUco marker detection | Mrugendra | 3 | Hour 9 | T1 | Done |
| T6 | PyGame map rendering + projector output | Mrugendra | 3 | Hour 12 | T5 | Done |
| T7 | Collision + goal detection logic | Mrugendra | 2 | Hour 14 | T6 | Done |
| T8 | Full system integration test | Both | 2 | Hour 15 | All | Done |
| T9 | Final documentation + README | Mrugendra | 1 | Hour 16 | All | Done |

### 10.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept | Mrugendra | Jyoti |
| Electronics | Jyoti | Mrugendra |
| Coding | Mrugendra | Jyoti |
| Mechanical build | Jyoti | Mrugendra |
| Testing | Both | Both |
| Documentation | Mrugendra | Jyoti |

---

## 11. Hour Milestones

### 11.1 8-Hour Plan

**Bi-Hour 1 — Plan and De-risk**
- ✅ Idea finalized
- ✅ Core interaction decided
- ✅ Sketches made
- ✅ BOM completed
- ✅ Purchase needs identified
- ✅ Key uncertainty identified (camera tracking accuracy)
- ✅ Basic feasibility tested (Pi WiFi + motor spin confirmed)

**Bi-Hour 2 — Build Subsystems**
- ✅ Electronics tests completed (motor direction, PWM speed)
- ✅ CAD / structure planning completed
- ✅ Flask web server running, phone can connect
- ✅ OpenCV ArUco detection working on test frame
- ✅ Main subsystems partially working independently

**Bi-Hour 3 — Integrate**
- ✅ Physical chassis built and wired
- ✅ Electronics integrated onto chassis
- ✅ Flask server connected to GPIO motor control
- ✅ Camera tracking feeding into PyGame coordinate system
- ✅ First driveable version exists with projection

**Bi-Hour 4 — Refine and Finish**
- ✅ Collision detection tuned
- ✅ Playtesting completed
- ✅ Visual feedback (red/green flashes) added
- ✅ Documentation completed
- ✅ Final build ready

---

## 12. Update Log

| Day | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Day 1 | Finalize concept, BOM, start chassis | Concept finalized, BOM done, chassis cutting completed | Decided to use webcam + ArUco instead of encoder-based tracking — simpler and more accurate | Start motor wiring and Flask server |
| Day 2 | Motor control working, Flask server live, OpenCV detecting marker | All three working independently by end of day | ArUco detection needed lighting adjustment — added a desk lamp over surface | Integrate camera data into PyGame |
| Day 3 | Full integration — car tracked live in game | Integration worked but projector alignment needed calibration | Added a calibration step at startup to map camera coordinates to projector coordinates | Tune collision zones, add visual feedback |
| Day 4 | Polish, playtesting, documentation | Car balancing issue found and fixed (added caster), playtesting done, docs completed | Simplified obstacle map after playtesting showed cluttered layout confused players | Final push to GitHub |

---

## 13. Risks and Unknowns

### 13.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| WiFi connection between phone and Pi becomes unstable | Technical | Medium | High | Keep Pi close, ensure stable power, add motor stop timeout if connection drops | Mrugendra |
| Camera tracking loses marker (occlusion, lighting) | Technical | Medium | High | Ensure consistent overhead lighting, use large printed ArUco marker | Mrugendra |
| Projector and camera coordinate systems don't align | Technical | High | High | Add startup calibration step using four corner reference points | Mrugendra |
| Car chassis not sturdy enough — flex or motor mount fails | Mechanical | Low | Medium | Laser cut parts glued + screwed, tested before full integration | Jyoti |
| Battery voltage sag causing Pi to reboot under motor load | Electrical | Medium | High | Buck converter with 3A rating, capacitors on motor terminals, tested under load | Jyoti |

### 13.2 Biggest Unknown Right Now
The projector-to-camera coordinate mapping. Both see the same physical surface but from different angles and with different distortions. Getting the projected obstacles to line up precisely with where the tracking system thinks boundaries are — that's the hardest calibration problem in the project.

---

## 14. Testing

### 14.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| WiFi motor control | Open phone controller, tap each direction, observe car | Car moves correctly in all four directions with < 200ms latency |
| ArUco marker detection | Move car by hand across surface, print position to terminal | Reported position matches actual position within ±2cm |
| Projector alignment | Place car at known position, check if projected grid matches | Car appears correctly on the projected map grid |
| Collision detection | Drive car into a projected obstacle wall | System triggers red flash within one frame of crossing the boundary |
| Goal detection | Drive car onto the projected target zone | System triggers green burst and loads next map |
| Motor timeout safety | Drop WiFi connection mid-drive | Car stops within 500ms |

### 14.2 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| 18th April | Car not balancing properly — tipping on turns | Mechanical | Added low-friction caster support to rear | Worked — stable on all surfaces | Improve caster mount for cleaner look |
| 19th April | ArUco detection failing under room lighting | Software | Added desk lamp directly above surface | Detection stable at 30fps | Keep lamp as part of setup |
| 20th April | Projector image misaligned with camera coordinates | Software | Added 4-point perspective calibration at startup | Alignment within ±1cm — acceptable | Document calibration steps for demo |
| 21st April | Motor stutter when Pi CPU load high (camera + server + PyGame) | Software | Moved motor commands to a dedicated thread with a queue | Stutter eliminated | Monitor CPU temp during long runs |

### 14.3 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| Gopal | Navigated through obstacles on Level 1 | Some obstacle walls weren't visually distinct enough | Loved the physical car + digital world interaction — felt genuinely magical | Added red highlight border around all obstacles |
| Sneha | Tried to reach target zone as fast as possible | Didn't know the car could reverse | The green burst on goal was very satisfying | Added reverse arrow to phone controller UI |

---

## 15. Build Documentation

### 15.1 Fabrication Process

**Design (CAD Modeling):** The chassis was modeled in CAD based on actual component dimensions — Pi, motor driver, battery pack, and motor positions were all dimensioned before cutting to ensure fit.

**Cutting (Laser Cutting):** Structural panels were laser cut from 3mm MDF sheets. Slots and tabs were designed for snap-fit assembly, reducing the need for fasteners.

**Assembly:** Components were fixed using a combination of hot glue and M3 screws. The motor mounts were kept removable (screw-only, no glue) to allow replacement. The Pi and motor driver were mounted on standoffs to allow airflow and easy rewiring.

**Surface Finishing:** Cut edges were sanded smooth. Gaps were filled with wood filler. The final chassis was painted matte black for cleaner aesthetics and to reduce reflections from the projector.

**Environment Setup:** A controlled surface was built using a white A3 board as the play area. A desk lamp was positioned overhead at 45° to ensure consistent, shadow-free lighting for ArUco tracking. The projector was ceiling-mounted at approximately 1 meter height for a 40×30cm projected game area.

**Revisions:** The original two-wheel drive design had a tipping problem on sharp turns — fixed by adding a rear caster wheel. The first ArUco marker (5cm) was too small for reliable detection at 1m camera height — reprinted at 8cm.

---

## 16. Build Photos

*[Upload the following and link here:]*
- Early chassis sketch
- Laser cut parts before assembly
- Wiring — Pi to motor driver
- ArUco marker mounted on car
- Projector and camera setup overhead
- First working drive test
- Final assembled car
- Full system running — car in projected battlefield

---

## 17. Final Outcome

### 17.1 Final Description
The final system is a two-wheeled RC car controlled via a phone web interface over WiFi. An overhead webcam tracks the car's position using an ArUco marker. A projector throws a top-down battlefield map onto the play surface. PyGame game logic runs on the Pi — detecting when the car hits obstacle zones (red flash) or reaches the target zone (green burst, next level loads). The experience is self-contained, portable, and playable by anyone in under 30 seconds with no instructions.

### 17.2 What Works Well
- Phone controller is instant and responsive — no noticeable lag
- ArUco tracking is stable and accurate under consistent lighting
- Projector calibration step reliably aligns digital and physical spaces
- Collision and goal detection feel snappy and satisfying
- The physical car + projected world combination consistently surprises and delights first-time users

### 17.3 What Still Needs Improvement
- Lighting dependency — system needs the desk lamp; ambient room light alone is not enough
- Projector must be mounted precisely — any movement breaks calibration
- Phone controller UI is minimal — could benefit from visual feedback (speed indicator, lives)
- Only two levels built — more maps needed for sustained play

### 17.4 What Changed From the Original Plan
The original idea used stepper motors and encoder-based position tracking (counting steps from a known origin). This was abandoned early when we realized camera-based ArUco tracking was far simpler, more accurate, and didn't require precise motor control. The pivot added the webcam to the BOM but removed the complexity of dead-reckoning navigation entirely. The PUBG battlefield framing was simplified — we focused on obstacle navigation rather than combat mechanics, which made the game logic much more achievable in the time available.

---

## 18. Reflection

### 18.1 Team Reflection
**What we did well:** We pivoted fast when the stepper motor plan wasn't working. We stayed focused on getting a working demo rather than adding features. The hardware/software split between team members worked cleanly — very little blocking.

**What slowed us down:** The projector calibration took far longer than expected — about 3 hours across two days of iteration. We underestimated how hard it is to reliably map two different cameras/projectors to the same coordinate system.

**Time and task management:** Generally good. The 2-hour block check-ins kept us honest. We dropped two stretch features (moving obstacles, multiplayer) to protect demo quality — the right call.

### 18.2 Technical Reflection
**Electronics:** Learned that motor load can cause real voltage instability — the buck converter and capacitors weren't an afterthought, they were necessary.

**Coding:** Threading in Python (motor control, camera feed, game loop all running simultaneously) was harder than expected. Queues between threads solved the stutter problem cleanly.

**Mechanisms:** Caster wheel for balance — obvious in hindsight, not obvious at design time. Always prototype balance before finalizing chassis.

**Fabrication:** Laser cut snap-fit tabs are excellent for rapid iteration but need tight tolerances — off by 0.2mm and parts don't fit.

**Integration:** The hardest part of any project is always when two independently working subsystems meet. Camera coordinates → projector coordinates is a solved problem (perspective transform) but it still took real time to get right.

### 18.3 Design Reflection
**Designing:** Simplicity of interaction (drive car, avoid walls, reach target) made the system immediately understandable. No tutorial needed.

**Delight:** The moment users first see the projected world respond to their physical car — that reaction is consistent and strong. Physical + digital interaction creates a specific kind of surprise that a screen alone doesn't.

**Clarity:** Early playtesting showed the obstacle walls needed more visual contrast. Added red borders immediately — shows that testing with real users early, even informally, always finds things you missed.

**Iteration:** The chassis went through two physical revisions and the software went through three major rewrites. That's normal. Build → test → learn → rebuild.

### 18.4 If We Had One More Hour
We would add a proper score and timer projected directly onto the surface — so the game state is fully visible without looking at a separate screen. It's the one thing that would make the experience feel complete and competitive.

---

## 19. Final Submission Checklist

- ✅ Team details are complete
- ✅ Project description is complete
- ✅ Inspiration sources are included
- ⬜ Sketches are added *(upload images)*
- ✅ BOM is complete
- ✅ Purchase list is complete
- ✅ Budget summary is complete
- ✅ Mechanical planning is documented
- ✅ App planning is documented
- ✅ Code flowchart is added
- ✅ Task breakdown is complete
- ✅ Update logs are complete
- ✅ Risk register is complete
- ✅ Testing log is updated
- ✅ Playtesting notes are included
- ⬜ Build photos are included *(upload images)*
- ✅ Final reflection is written
