---
title: "Opinions and Unsolicited Advice"
author: avishek
usemathjax: true
tags: ["Software Engineering", "Value System"]
draft: true
---

This is a weird mix of advice I'd give the less-experienced me, as well as reflections of my personal value system. This verbal diarrhoea came out all at once in a single sitting of 45 minutes. I apologise for some of the strong language in here, but I thought I'd share it without much censoring.

This post sums up a lot of my core beliefs and reflects many of my biases, so it's not necessarily "good" advice; it's just things I would share with someone I was mentoring. All of these are personal opinions.

Happy Reading!

### On Learning and Abstractions

- **Learning underpins engineering.** This can either be from an engineering aspect or from a strategy aspect. Everything is learnable, it mostly depends upon what you are primarily drawn to. Whether it is building executive messaging skills, building connections, or nudging people towards their stated goals, all of these are within your cognitive abilities.
- **Learn upwards.** These include things that we consider "bullshit skills". However, these are the skills which make people feel warm and fuzzy and more inclined to cooperate with you / not be hostile towards you. in order to get your job done. These are the skills that will help you in discussions with clients, internal management. If it helps you to think more like an engineer, this is the tech stack for communicating with humans, who are sometimes illogical, ego-driven, and frequently have goals different from yours.
- **Learn downwards.** Always keep learning new technical things. Things which drive you. If you have found yourself in a position which prevents you from doing programming that you like, find time to do that outside. Or pick other things which will still exercise your brain (I study pure math to keep my brain from rotting). But keep learning. This is a non-negotiable. Do not call yourself an engineer otherwise, just a person who is collecting a paycheck (which is also fine, btw. I don't judge, but that's contrary to my value system). See [Resilient Knowledge Bases : Fundamentals, not Buzzwords]({% post_url 2021-11-06-resilient-knowledge-bases %}) for some thoughts on the nature of things that I think you should focus on.
- *But, most importantly, learn upwards.* The upwards skills will seem useless, difficult to put into practice, and do not guarantee results in every situation. See the next couple of points on why this is still worth investing in.
- **Engineers must learn to abstract.** Keep learning consulting tools. Bigshots want the 10,000 feet view and hate processing details. Think of them as just programmers who are working at a higher level of abstraction. Imagine if you had to understand what the circuits of the computer were doing every time you wrote a single line of code in your favourite programming language. Invest in moving to a higher level of abstraction when expressing your thoughts. This ties into the skills needed to get a seat at higher levels of decision-making.

### On Decision-Making and Influencing
- **Engineers should -- and must -- have control and a say in strategic decisions.** They must have a voice at every level of management. Products and services do not exist without the work of engineers. Engineers are not order takers -- YOU are not an order taker. You may take advice, but not orders. Accordingly, if on your account, if there are decisions being taken which affect you and/or your team, and you do not have an engineering voice at the table, question, Question, QUESTION. Get yourself (or someone you trust on to the table). If you do not do this, someone will make your decisions for you. I don't think you'd like that. You may think that all you really need is to build great software, but this is the consulting industry. Simply building good software is not enough. There is client perception management, there's internal perception management, there's a lot of bullshit going on, and some people thrive on it. Some people get used to it. Some people navigate through them. You are no exception. Understand that you can choose to ignore these factors, but these factors will not ignore you.
- In accordance with the above point, I believe that there is one fundamental duty that engineers have: and that is to **clarify this reality to less experienced engineers who are more focussed on developing their hard skills**. Not educating our peers about this can lead to a vicious cycle of engineers relegated to executors of other people's visions. You don't want that. Fuck that noise. Strategic decisions are too important to be left to bigshots and nontechnical people.
- However, before you go running off into the wild, hysterically demanding a seat at every table, it is important to understand the **appropriate language at the appropriate level of abstraction**. I touched on the topic of abstraction above, but let us expand on this a little further. The language I am talking about is the **language of economics**. Indeed, most important decisions taken at the organisation level are always against the backdrop of profit/loss, discounted cash flows, albeit with a technological bent. In fact, there continues to be a wide disconnect between the mindset which most software developers make decisions, and how executives make their decisions. This usually shows up as distrust and disbelief around estimates, friction and frustration around value articulation, and so on. My increasingly strengthening belief is that all software engineers should think relentlessly like economists. There are several practices in agile development which encourage this mindset, but my contention is that the spirit of the concept is lost behind mindless practice, and that there is much more that developers and architects could -- and should -- do to bridge this gap.
- **Engineers must learn to think in terms of options.** Too many times, engineering viewpoints are overridden by financial considerations, revenue considerations, delivery considerations, because, very rightly, the decision-makers are thinking inside a different framework. Actually, most of the time, everything translates to money. Thus, it behooves you to always think in terms of a spectrum of options, starting with "cheapest-shittiest" to "expensive-elegant". Understand that you are the custodian of pulling the slider in the direction of "expensive-elegant", while the bean-counters are looking for "cheapest-shittiest" but won't always say that out loud, usually couching it in more diplomatic terms like "we'll pay off the tech debt later", "there needs to be a more creative solution" (Have I mentioned how much I hate it when people mention "creative"?). There are several ways this can be achieved. I outline the beginnings of one which leverages the economics-based frameworks to guide and project engineering decisions. See [here]({% post_url 2023-01-22-every-developer-is-an-economist %}).

### On Building Engineering Culture
- **Culture, particularly engineering culture, cannot flourish in a vacuum.** It must be aggressively nurtured. Nurturing is not about deciding to do things by committee. It needs to be fostered by example. If you do not see the culture you want to be in, you have 4 options: 1) wither away full of regret in an unfulfilling environment, 2) take steps to lead by example, 3) instill culture by fiat (never really works, so I don't even know why I put this as an option), 4) leave. (4) is the nuclear option. (1) is the do-nothing option. (2) is sort of a gamble, because its success doesn't simply depend upon your skill. It also depends upon your personality, how you showcase your examples, how you include people. Reputation naturally grows from the quality of your work, but management is continuously eyeing you as an untapped opportunity to train the next generation of technologists.
- **Decide how much you want to invest in facilitating building culture without sacrificing your own personal goals.** Remember that your personal goals are always the most important; stay true to them, but remember that they are not the only ones. In most cases, as an engineer (unless you are actively planning to go completely hands-off), your personal goals will not align with what the organisation really expects you to do (to justify your billing rates). It is a constant trade-off between what you'd really rather be doing vs. what you feel you must do to advance in your organisation (whether your motivation is money, the corporate ladder, or whatever). Make that conscious decision, but MAKE it. Don't stagnate.

### On Performance Reviews
- On that same note, **performance reviews are bullshit and mostly performative**. Half of it is based on the fantasies people have of what the perfect person in your role will be doing, and the other half is ticking checkboxes to satisfy some inane requirement that we are helping everyone grow. To be honest, you cannot really blame management, because performance reviews are literally the only shortcut that they can think of whenever they want to know if they are wringing the maximum value out of people, in a large scaling organisation. (Btw, Dunbar's Number is disputed heavily in later studies; another example of how corporate thinking clings on to buzzwords without examining new evidence; see https://royalsocietypublishing.org/doi/10.1098/rsbl.2021.0158). Instead, find yourself a set of people whose work you really admire; this work can be upward-focussed and/or downward-focussed. Compare yourself against these people. Ask them. Learn by imitation. If you get to a point where you start doing some of the things you weren't doing before because of these people, you have improved. Full stop.
- On the flip side, organisation performance reviews are good for one thing: **they act as reminders in case you are really drifting somewhat aimlessly**. Repurpose this inane bureaucratic exercise to your own liking otherwise, as you see fit. Put the goals that you are really interested in and work through those at your own (hopefully motivated) pace. There will always be organisational goals that you will be expected to work towards too. Take those as opportunities to learn those upwards-facing skills, and try things which are outside your comfort zone. Remember, try anything once. You don't have to like it, and you can stop doing it after a couple of review cycles. You always have a choice to say "No" in doing something; the consequences are never as dire as you fear.


### For Introverts
This section is specifically for introverts, since I am one myself.

- **Do not let anyone pressure you into making an on-the-spot engineering decision.** Firmly say "I need to think about it".
- **Be shameless in interrupting.** Extroverted, consulting types hog a lot of time and think nothing of it. You are not being rude in interrupting in order to get your point across. People do it all the time, and are hailed as being assertive. So go be "assertive".
- If you are thinking, and someone interrupts, feel free to excuse yourself and walk away and continue your thought. People do not respect the state of flow, knowingly or unknowingly (even engineers aren't telepaths), and they need to be firmly reminded that this is not acceptable.