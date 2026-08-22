# Jenkins Freestyle Project: Clone & Install

## Hands-On: Create a Freestyle Job

### Step 1: Create New Freestyle Project
1. Go to Jenkins Dashboard
2. Click **"New Item"**
3. Enter name: `freestyle-clone-install`
4. Select **"Freestyle project"**
5. Click **"OK"**

### Step 2: Add Build Step 1 - Clone
Under **Build Steps**, click **"Add build step"** > **"Execute shell"**:
```bash
# Clean up any residual files from previous builds and clone cleanly
rm -rf devopshift-welcome
git clone -b jenkins-workshop https://github.com/yanivomc/devopshift-welcome.git
```

### Step 3: Add Build Step 2 - Install
Click **"Add build step"** > **"Execute shell"** again:
```bash
# Move into the Flask app subfolder and install requirements
cd devopshift-welcome/welcome/app/flask-volt-dashboard
pip install --user -r requirements.txt
```

### Step 4: Run the Job
1. Click **"Save"**
2. Click **"Build Now"**
3. Check **"Console Output"** to see the clone and install succeed

### Step 5 (optional): Launch the App
Add a third **"Execute shell"** build step. Run it backgrounded so the build doesn't hang forever waiting on the dev server:
```bash
cd devopshift-welcome/welcome/app/flask-volt-dashboard
pkill -f "python3 run.py" || true
sed -i "s/app\.run(.*)/app.run(host='0.0.0.0', port=5000)/" run.py
nohup python3 run.py > /tmp/flask-app.log 2>&1 &
sleep 2
cat /tmp/flask-app.log
```
Open `http://<agent-host>:5000` in your browser. The log printed above should say `Running on http://0.0.0.0:5000` — if it still shows `127.0.0.1`, an old instance was left running from a previous build; the `pkill` line now clears that before relaunching.

---
### **Next Steps**
<a href="../03-helloworld/README.md">Hello World Pipeline</a>
