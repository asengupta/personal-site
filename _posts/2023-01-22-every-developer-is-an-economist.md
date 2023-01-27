---
title: "Every Software Engineer is an Economist"
author: avishek
usemathjax: true
tags: ["Software Engineering", "Economics"]
draft: false
---

Background: This post took me a while to write: much of this is motivated by problems that I've noticed teams facing day-to-day at work. To be clear, this post does not offer a solution; only some thoughts, and maybe a path forward in aligning developers' and architects' thinking more closely with the frameworks used by people controlling the purse-strings of software development projects.

The other caveat is that this article does not touch the topic of estimation. That is intentional; I won't be extolling the virtues or limitations of #NoEstimates, for example (sidebar: the smoothest teams I've worked with essentially dispensed with estimation).

**Every software engineer is an economist; an architect, even more so.** There is a wealth of literature around articulating value of software development, and in fact, several agile development principles embody some of these, but I see two issues in my day-to-day interactions with software engineers and architects.

- Folks are reluctant to quantify things they build, beyond the standard practices they have been brought up on (like estimation exercises, test coverage). Some of this can be attributed to their prior bad experiences of being micromanaged via largely meaningless metrics.
- Folks struggle to articulate value beyond a certain point to stakeholders who demand a certain measure of rigour and/or quantifiability. The DORA metrics are good starter indicators, but I contend that they are not enough.
- There is a reluctance to rely too much on metrics because people think metrics are easily gamed. This can be avoided if we use econometric methods, because 1) falsified data is immediately apparent 2) showing the work steps, assumptions and risks aids in this transparency because they are in the language of economics which is much more easily understandable to business stakeholders.
- Thinking about value and deciding tradeoffs based on economic factors is not something that is done enough, if at all, at the level of engineering teams. For example, questions like "Should I do this refactoring?" and "Why should we repay this tech debt?", or "How are we better at this versus our competitor?" are usually framed in terms of statements which stop before traversing the full utility tree of value.

Thinking in these terms, and projecting these decisions in these terms to micromanagers, heads/directors of engineering -- but most importantly, to execs -- is key to engineers articulating value in a manner which is compelling, and eases friction between engineering and executive management. It is also a value engineers should acquire to break several firms' perceptions that "engineers are here to do what we say".

This is easier said than done, because of several factors:

- The data to apply these frameworks is not always easily available, or people are not ready to gather that data.
- Engineers are usually emotionally invested in decisions that they think are their "pet" ideas.
- It can be hard to inculcate this mindset en masse among engineers if they do not have a clear perception of the value of adopting this mindset. Engineers don't want theory, they want tools they can apply quickly and easily. Hence the burden is on us to propose advances to the state of the art in a way that is actionable.

Important Concepts that every software developer should know:

- Decision-Making Processes
  - Analytic Hierarchy Process
- Utility-based Architecture Decision Making: CBAM
  - [The CBAM: A Quantitative Approach to Architecture Design Decision Making](https://people.ece.ubc.ca/matei/EECE417/BASS/ch12.html)
  - [Making Architecture Design Decisions: An Economic Approach](https://apps.dtic.mil/sti/pdfs/ADA408740.pdf)
  - The above goes some way towards assigning utility to architectural decisions. These are at the level of Cross-Functional Requirements, and DORA metrics, but do not point the way towards calculating financial implications.
- Net Present Value and Discounted Cash Flows

### Deriving Value in Legacy Modernisation

$$C_{HW}$$ = Cost of Hardware / Hosting \\
$$C_{HUF}$$ = Cost of manual work equivalent of feature (if completely new feature or if feature has manual interventions) \\
$$C_{RED}$$ = Cost of recovery, including human investments (related to MTTR) \\
$$C_{LBD}$$ = Cost of lost business / productivity during downtime (related to MTTR) \\
$$C_{ENF}$$ = Cost of development of an enhancement to a feature (related to DORA Lead Time) \\
$$C_{NUF}$$ = Cost of development of a new feature (related to DORA Lead Time) \\
$$C_{BUG}$$ = Cost of bug fixes for feature \\
$$n_D$$ = Number of downtime incidents per year \\
$$n_E$$ = Number of enhancements to feature per year \\
$$n_B$$ = Number of bugs in feature per year

The cost of a feature is then denoted by $$V$$, and the total value of the feature is $$V_{total}$$. These are given by:

$$
V=C_{HUF} + n_D.(C_{RED} + C_{LBD}) + n_E.C_{ENF} + n_B.C_{BUG} \\
V_{total} = \sum_{i} V_i + C_{HW} + n_F.C_{NUF}
$$

Retention of customer base is also a valid use case. Not sure how to quantify this...

### Real Options

We will not discuss the Options Thinking approach from scratch here; rather we will delve into some of its possible applications in architectural decision-making and technical debt repayment. See the following for excellent discussions on the topic:

- [Software Design Decisions as Real Options](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=24f7bdda5f3721faa2da58719ae72432f782312f)
- [The Software Architect Elevator](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)
- Chapter 4 of [Extreme Programming Perspectives](https://www.amazon.com/Extreme-Programming-Perspectives-Michele-Marchesi/dp/0201770059)
- Chapter 3 of [Value-Based Software Engineering](https://link.springer.com/book/10.1007/3-540-29263-2)


- 
- Disadvantages of the NPV approach
- Opportunity Cost
- Examples
  - One example where we could have applied: The team had built a data engineering pipeline using Spark and Scala. The stakeholder felt that hiring developers with the requisite skillsets would be hard, and wanted to move to plain Java-based processing. A combination of cash flow modeling and buying the option of redesign would have probably made for a compelling case.

## Incorporating economics into daily architectural thinking

Here are some generic tips.

- Practise drawing causal graphs. Complete the trace all the way up to where the perceived benefit is (money) is. It may be tempting to stop if you reach a DORA metric. Don't; get to the money.
- If you are already measuring DORA metrics, relentlessly ask what each DORA metric translates to in terms of money.
- Along the way of the graph, list out other incidental cash outflows.
- Remember that story points must always be converted into hours to actually be incorporated into economic estimates.
- CALCULATE NPV!!! HOW?
- Build Options tree. Deduce whether it is better to defer execution, or do it right now.

Here are some tips for specific but standard cases.

#### 1. The Economics of Microservices

If you are suggesting a new microservice for processing payments, these might be the new cash flows:
  - Recurring Cash Flows
    - Transactions: New cash inflow
    - Cost of recovering the whole system back from failure: Reduced cash outflow
    - Cost of cloud resources to scale the new microservice: New cash outflow
    - Cost of higher latency leading to lower service capacity (if the microservice is part of a workflow): Decreased cash inflow, depending upon if you ever reach the load limits of the service before other parts of the system start to fail
    - Cost of fixing bugs: New cash outflow, depending upon complexity of the microservice
    - Cost of Integrations: 
- Single or Few-Time Cash Flows
  - Cost of development: New cash outflow
  - Cost of deployment setup: New cash outflow (ideally should be as low as possible)

**Causal Graph**

{% mermaid %}
graph LR;
debt[Tech Debt]-->principal[Cost of Fixing Debt: Principal];
debt-->interest[Recurring Cost: Interest];
debt-->risk[Risk-Related Cost];
architecture_decision[Architecture Decision]-->resources[Cloud Resources];
microservice-->database[Cloud DB Resources];
microservice-->development_cost[Development Cost];
microservice-->latency[Latency];
microservice-->bugs[Fixing bugs];
microservice-->downtime[Downtime]-->lost_transactions[Lesser Lost Transactions];

style chol fill:#006f00,stroke:#000,stroke-width:2px,color:#fff
style mvn fill:#006fff,stroke:#000,stroke-width:2px,color:#fff
style gp fill:#8f0f00,stroke:#000,stroke-width:2px,color:#fff
{% endmermaid %}

#### 1. The Economics of Technical Debt repayment
- Recurring Cash Flows
  - Cost of Manual Troubleshooting and Resolution
  - Cost of recurring change to a specific module
- Single or Few-Time Cash Flows
  - Cost of repaying tech debt

**Valuing Real Options using [Datar-Matthews](https://www.researchgate.net/publication/227374121_A_Practical_Method_for_Valuing_Real_Options_The_Boeing_Approach)**

#### 1. The Economics of New Features

### References

- [Economics-Driven Software Architecture](https://www.amazon.in/Economics-Driven-Software-Architecture-Ivan-Mistrik/dp/0124104649)
- [Software Design Decisions as Real Options](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=24f7bdda5f3721faa2da58719ae72432f782312f)
- [A Practical Method for Valuing Real Options: The Boeing Approach](https://www.researchgate.net/publication/227374121_A_Practical_Method_for_Valuing_Real_Options_The_Boeing_Approach)
- [How to Measure Anything](https://www.amazon.in/How-Measure-Anything-Intangibles-Business/dp/1118539273)
- [Excellent Video on Real Options ECO423: IIT Kanpur](https://www.youtube.com/watch?v=lwoCGAqv5RU)
