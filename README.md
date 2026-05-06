# AI Network Analyzer Dashboard

## About this project

This is a simple AI-based project where I tried to understand how network usage can be monitored and analyzed.

The system checks internet usage and number of devices, and then tells whether the behavior is normal or abnormal.

I also created a live dashboard to show the data in real time.

---

## Why I made this

Sometimes we don’t know why internet becomes slow.

It can be because:

* too many devices
* very high usage by few devices

So I wanted to build a system that can detect this using AI.

---

## How it works (simple)

1. I created a dataset based on real-life situations
2. Trained a machine learning model using RandomForest
3. Backend API sends usage + device data to model
4. Model predicts:

   * Normal
   * Abnormal
5. Frontend dashboard shows:

   * usage
   * number of devices
   * alert message
   * graph

---

## Example

If devices = 2
and usage = 300

Then output = Abnormal

Because high usage with few devices is not normal.

---

## Tech used

* Python
* FastAPI (for backend API)
* scikit-learn (for ML model)
* HTML, CSS, JavaScript (frontend)
* Chart.js (for graph)

---

## What AI is doing here

AI is learning normal patterns.

Example:

* 2 devices + low usage → normal
* 2 devices + very high usage → abnormal

So instead of writing hard rules, model learns patterns automatically.

---

## Features

* Detect abnormal usage
* Real-time dashboard
* Color alerts (green/red)
* Live graph
* Smooth animation and glow effect

---

## Limitations (important)

Currently this project uses simulated data.

It does NOT yet connect to real router data.

---

## Future improvements

In future, I want to:

* connect with real router data (like OpenWrt)
* track per-device usage
* detect which website is using more data
* store history in database
* add login system

---

## What I learned

* how to train ML model
* how backend and frontend connect
* how real-time data can be visualized
* how AI can be used in network monitoring

---

## Author

This project is created by me for learning purpose.

I tried to keep everything simple and understandable.
