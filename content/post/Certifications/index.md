---
title: 2025 Certifications
description: This page contains my review on the certifications I took this year, including CMPen (iOS & Android), Pentest+, CRTA, PT1 and CPTS.
date: 2025-08-12 00:00:00+0000
categories:
   - Certifications
tags:
   - Certifications
weight: 1     
---
Let’s rewind to the start of the year and walk through my certification journey so far. 

---

## **CPTS Preparation: My HTB Marathon**  

Originally, I planned to take the **CPTS** after PwC HackADay. My "preparation" was basically grinding HTB rank and I started in December 2024 until recently, not sure if I wanna stop the grind tho, since I already have CPTS. I went through every single ***easy*** and ***medium*** box during that time, missing only one or two due to Chinese New Year or other unskippable events.  

Interestingly, every Windows box during this period (except one) was **Active Directory** related. My AD skills skyrocketed because of it. But throughout this time, I didn't bother with hard or insane boxes because HTB's difficulty ratings just mean 'more steps'. In simplest terms, a medium box will have more 'steps' in its attack chain than an easy box will, a hard box will have more 'steps' in its attack chain than a medium box will, etc. And because of this, doing a hard box normally takes more time then 2 medium box combined. So my logic was simple: ***two mediums = one hard***. Why spend time on one "hard" when I can knock out two mediums and learn just as much?  

---

## **The SecOps CMPen iOS**  

This was an impulse buy, thanks to a 90% discount. The exam was fully hands-on: you’re given an **IPA file** and have to hack it, finding “flags” along the way.  

I relied heavily on the [OWASP MASTG](https://mas.owasp.org/MASTG/) as my guide. The exam questions are not directly related to MASTG tho, but I used the test cases and passed. Sounds simple, but it was tougher than expected, I needed two attempts to just barely passed. Definitely a humbling start.  

---

## **The SecOps CMPen Android**  

Another 90% discount, so… why not? Same deal as iOS, but this time with an **APK file**. I used the same MASTG approach and found the flags. This one felt easier than iOS, and my score reflected that, though I’d still call it a "barely passed".  

---

## **CompTIA Pentest+**  

This one was a surprise win. During MCC, I actually won **Security+**, but I was able to redeem **Pentest+** with the voucher given to me, so why not. I definitely overprepared for this and I was able to  finish the MCQ exam in 20 minutes with flying colours. The format makes it forgiving: because it is MCQ, even if you don't know the answer, you can eliminate the obviously wrong ones.  

---

## **Cyber Warefare Labs CRTA**  

I took the **Certified Red Team Analyst** because I wanna see  how far my CPTS prep had gotten me. But turns out CRTA was easier than an easy box on HTB. The exam is fully hands-on: you get a network, compromise it, and capture flags. It's straightforward, no guesswork, covering Linux and AD. 

---

## **TryHackMe Junior Penetration Tester**  

Earlier this year, TryHackMe gave away **PT1** to folks with Pentest+, OSCP, and other similar certs. The exam covers:  

- Linux privilege escalation  
- Windows privilege escalation  
- Active Directory  
- Web  

AD and Linux/Windows privilege escalation was easy and I was able cleared them in about six hours. The **web** part, though, was a nightmare. It says its web, but its more towards API than web. Their XSS scenario was unrealistic (even some CTFs feel more realistic), and their "half-flag" concept was so confusing that I still couldnt figure it out after the exam, maybe someone who took PT1 can tell me. The IDOR setup also doesn't make sense to me. To anyone who wishes to take PT1, please read the ROE at the start, it explains how their XSS works and lists all possible web (API) vulnerabilities.  

---

## **HTB CPTS**  

So after all those ranked HTB, I started CPTS at the end of July 2025 and took about 7 days to capture 14 flags and finish my report. You need 12 flags to pass and there is a total of 14 flags to capture. You actually don't need to capture all 14 flags, as 12 flags is enough to pass, but that also depends on your reporting.

It feels like 7 medium HTB boxes chained together. Pivoting is definitely needed, so for anyone taking it, please learn the basics of pivoting, any form of pivoting works I believe, as I used a combination of a few during the exam.  

- **Web**: My biggest weakness as I am absolutely dog shit in web. Every time I got stuck, it was web.  
- **Linux PrivEsc**: Straightforward.  
- **Windows PrivEsc**: Slightly harder than Linux but still manageable.  
- **Active Directory**: Normally I use Linux for AD work, but during the exam I hit weird NetBIOS issues with CME/NXC. I had to switch to Windows tools, which slowed me down, but at least my module practice paid off.  

All in all, CPTS was fun, balanced, and a great skill test.  

---

## Final Thoughts  

hehe, back to CTFs now.