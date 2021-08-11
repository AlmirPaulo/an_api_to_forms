# An API to Forms
An API to Forms. Yeah, I could not come out with a better name... Sorry. I hope it serves you, anyway. 
This API can works as a backend to your forms. It's perfect for static pages.

## Features
By now the only feature is email sending.

## How to use it

1. Clone this repository.

2. Set the right values on the **config.py** variables.

3. Deploy it.

4. Code your form and paste the url of your deployed server to the action attribute, like this:

        <form action="yourwebserveraddress.domain" method="POST">
            ...
        </form>

## The Email Sending Feature

Use the */email* endpoint and code your form more or less like this:

        <form action="yourwebserveraddress.domain/email" method="POST">
            <input type="text" name="subject" placeholder="Subject" required>
            <input type="text" name="email" placeholder="Email" required>
            <textarea name="text" cols="30" rows="10" required></textarea>
            <button type="submit" onclick="alert(Email sent!)">Send</button>
        </form>
The important part is the *name values*, the *method* and the *action url*. All the rest is just suggestions.

## Plans for the future

- [ ] Authentication handling
- [ ] Collecting data forms 

## F.A.Q.

1. Why you do not deploy an instance to handle everbody's forms?

There is services like this out there. But if you, like me, like to have more control over your data, maybe you would like to use an alternative like this.

2. What about my password or sensible datas?

You probably can hide this in the server using environment variables. Another good ideia is to use an app password, if your email is at gmail.

3. If a find any bug...

Open an Issue please.

## Contribute
## Release
### 0.0.1 - August 11, 2021

First Release
