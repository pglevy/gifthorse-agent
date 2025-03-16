# GiftHorse

A gift-sharing app for families and friends, vibe-coded with the Replit AI Agent

## Why
Every year as the holiday season approached, it was the same routine: my mom would start an email thread asking about what gifts everyone wanted. And every year, we ran into the same problem: managing replies and side chats to figure out who was doing what while maintain some semblance of surprise.

A couple years ago, I decided to do something about it and built a gift sharing app using the no-code platform Glide Apps. This worked well enough, but as I had become more comfortable with coding and seen what was possible with AI, this year I embarked on re-building the app from scratch.

## How
In addition to using this as an excuse to learn more about pair programming with AI, I was also interested in the additional flexibility and freedom of moving off a platform and owning my own code. I had been playing around with Replit, working through their Learn to Code (Python) material and really liked the overall quality of their product. It already had AI chat built in, so it was possible to ask questions and piece things together yourself. But I would still hit snags with things like authentication and database connections.

Once their Agent became available and I tried out some basic examples, the path forward was clear: have the agent build a boilerplate app with all the hard stuff already working, and then add on features to incrementally get to what I wanted — just like building software with a dev team!

## What
The recommendation when using Agent was to let go of preferences like the tech stack and focus on the functionality. So I started with asking for a simple CRUD app for users to manage their profile and then started adding features with prompts like, “let people create a wish list of items” and “create a shopping list where people can see the items other people want, but not their own.” The Agent selected Python with Flask and Postgres (with some basic hand-rolled CSS), and got to work. Occasionally, there were some glitches, but I would point them out and it would iron out the bugs along the way. Once the core functionality was working, I hopped in to add a minimal CSS framework (Pico) to level-up the layout and tweak some interactions.

So far it’s working beautifully, with family members adding items to their wish lists and others claiming them off the shopping list. Of course, there’s user feedback and things to fix or improve as with any software product. After working in enterprise UX for years, where we are often disconnected from our users, it’s really fun to see someone use something you’ve built, give direct feedback, and then make a change and re-deploy it within minutes. While there will always be a need for a professional developers, this seems like the future of custom software: exactly what you need when you need it.

## Screenshots

The home, item edit, comment, and shopping list screens:

<img src="https://github.com/user-attachments/assets/570f97f3-a407-4cfa-a1dc-7a8d6f60b963" width="400" alt="home screen">
<img src="https://github.com/user-attachments/assets/b69ae758-3dda-4292-b162-5fe347a34922" width="400" alt="edit item screen">
<img src="https://github.com/user-attachments/assets/87013970-d7f0-48a9-98fb-8f5728d807d3" width="400" alt="comment screen">
<img src="https://github.com/user-attachments/assets/8f65ce27-4661-4c5c-9914-4c3f0b497e9d" width="400" alt="shopping list screen">
