<template>
  <div>
    <h1 class="info-title">Decisions made easy.</h1>
    <h2 class="what-is">What is decidOR?</h2>
    <p class="whatis-text">
      Can't decide what to do, where to eat, or what to watch?
      decidOR provides a guided experience that enables users to easily make a variety of common decisions when faced with an overwhelming amount of choices. Our application simplifies this process by presenting two options at a time, in order for the user to reach an ultimate decision.
    </p>
    <div class="screenshots-div">
    <img class="screenshot" id="choices-screenshot" src="//decidor.s3.us-east-2.amazonaws.com/choices_screen.png" />
    <img class="screenshot" id="final-screenshot" src="//decidor.s3.us-east-2.amazonaws.com/final_choice.png" />
    <div>
  
    <h3 class="what-is">How to Use decidOR</h3>
    <p class="whatis-text">
      Start by choosing from one of our Decks: curated collections of common options to choose from.
      Our "bracket-style" algorithm will guide you through the process by presenting you with two options at a time. Keep picking the one you prefer until you arrive at your final decision. A progress bar indicates how far your are through the process, while the color of the bar changes each time you enter a new round of preferences.
    </p>
      </div>
</template>

<script>
import Info from "./Info.vue";

export default {
  name: "info",
  components: {
  }
};
</script>