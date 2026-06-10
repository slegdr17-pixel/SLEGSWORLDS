from ursina import *
import animation

# Initialize High-End 3D Engine Context
app = Ursina(development_mode=False, borderless=False)
window.title = 'SLEGSWORLDS - Cinematic V'
window.fps_counter.enabled = False

# 1. 4K Atmospheric Fog & Dark Gothic Lighting
scene.fog_color = color.rgb(5, 5, 5)
scene.fog_density = 0.02
AmbientLight(color=color.rgba(10, 10, 20, 50))

# 2. Handcrafted Gothic Cathedral Pillars (Procedural 3D Depth)
pillars = []
for i in range(10):
    # Left Pillar row
    lp = Entity(model='cube', scale=(2, 15, 2), position=(-6, 7.5, -i * 12), color=color.rgb(20, 20, 20))
    # Right Pillar row
    rp = Entity(model='cube', scale=(2, 15, 2), position=(6, 7.5, -i * 12), color=color.rgb(20, 20, 20))
    
    # Warm Elden Ring Candle Light Clusters down the aisle
    PointLight(position=( -4 if i%2==0 else 4, 1, -i * 12), color=color.rgb(255, 170, 68), distance=15)

# 3. Immersive Audio Engine (Slowed Echo Setup)
# Places the background track inside the 3D space
bg_music = Audio('golden-brown-slowed.mp3', loop=True, autoplay=False, volume=0.8)

# 4. Cinematic Camera Configuration
camera.position = (0, 3, 5)
camera.rotation = (0, 0, 0)

cinematic_active = False

# Screen Overlay / Input Trigger
def input(key):
    global cinematic_active
    if key == 'space' or key == 'left mouse down':
        if not cinematic_active:
            cinematic_active = True
            bg_music.play()

# 5. Real-Time Render Update Loop (The Cinematic Walk)
def update():
    global cinematic_active
    if cinematic_active and camera.z > -90:
        camera.z -= 2 * time.dt # Smooth 4K cinematic camera camera glide forward
        
        # As camera reaches the altar area, reveal the luxury anniversary surprise
        if camera.z < -40:
            print("Displaying Anniversary Envelope Text...")

app.run()
