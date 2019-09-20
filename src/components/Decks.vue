<template>
  <section>
    <h1 class="page-title" :class="{ hiddenDick:hiddenTitle }">What can we help you decide?</h1>
    <div class="deck">
      <div v-if="!hiddenSearch" class="searchBar">
        <label class="searchPrompt" for="location-search">Where would you like to find choices?</label>
        <div>
          <input
            class="input"
            id="location-search"
            type="text"
            v-model="cityName"
            v-on:keyup.enter="getBusinesses"
            placeholder=" Address, City, Zip Code, etc..."
          />
          <button
            :disabled="cityName.length < 3"
            class="searchButton"
            @click="getBusinesses"
          >TYPE STUFF</button>
        </div>
        <img class="orLogo" src="//decidor.s3.amazonaws.com/OR_solid_white.png" alt="OR" />
        <button class="locationButton" @click="getLocation()">Get My Location For Me</button>
      </div>

      <div v-if="!hiddenCustomSearch">
        <article class="customSearchGrid">
          <label
            id="custom-search-head"
            class="searchPrompt"
            for="custom-term-search"
          >What are you looking for?</label>
          <input
            class="input"
            id="custom-term-search"
            type="text"
            v-model="searchTerm"
            placeholder=" Coffee, bookstores, etc..."
          />
          <label
            class="searchPrompt"
            for="custom-location-search"
            id="find-choices-head"
          >Where would you like to find choices?</label>
          <input
            class="input"
            id="custom-location-search"
            type="text"
            v-model="cityName"
            v-on:keyup.enter="getBusinesses"
            placeholder="Address, City, Zip Code, etc..."
          />
          <button
            id="get-choices-custom"
            :disabled="cityName.length && searchTerm.length < 3"
            class="searchButton"
            @click="getBusinesses"
          >TYPE STUFF</button>
          <span id="or-logo-custom" class="orLogo">or</span>
          <button
            id="location-custom-butt"
            class="locationButton"
            :disabled="searchTerm.length < 1"
            @click="getLocation()"
          >Get my location for me</button>
        </article>
      </div>

      <!-- <div v-if="!hiddenMovieSearch" class="searchBar">
        <label class="searchPrompt" for="movie-location-search">Where would you like to find movies?</label>
        <div class='help'>
          <input
            class="input"
            id="movie-location-search"
            type="text"
            v-model="cityName"
            v-on:keyup.enter="getCityID()"
            placeholder="City Name"
          />
          <button :disabled='cityName.length < 3' class="searchButton phone" @click="getCityID()">TYPE STUFF</button>
        </div>
        <img class="orLogo" id="movie-or-logo" src="//decidor.s3.amazonaws.com/OR_solid_white.png" alt="OR" />
        <button class="locationButton" id="movie-location-button" @click="getMovieLocation()">Get My Location For Me</button>
      </div>-->

      <!-- <div v-if="!hiddenMovies">
        <ChoiceLogic :choices="allDecks.inTheaters" />
      </div>-->

      <div v-if="!hiddenNetflix">
        <ChoiceLogic :choices="allDecks.netflixDeck" />
      </div>

      <div v-if="!hiddenNetflixFilms">
        <ChoiceLogic :choices="allDecks.netflixFilmsDeck" />
      </div>

      <div v-if="!hiddenFictionBooks">
        <ChoiceLogic :choices="allDecks.fictionDeck" />
      </div>

      <div v-if="!hiddenNonFictionBooks">
        <ChoiceLogic :choices="allDecks.nonFictionDeck" />
      </div>

      <div v-if="!hiddenBusiness">
        <ChoiceLogic :choices="allDecks.yelpRestaurants" />
      </div>

      <div v-if="!hiddenFood">
        <ChoiceLogic :choices="allDecks.fastFoodDeck" />
      </div>

      <div v-if="!hiddenFoodTypes">
        <ChoiceLogic :choices="allDecks.foodTypesDeck" />
      </div>

      <div v-if="!hiddenMilkshakes">
        <ChoiceLogic :choices="allDecks.cookoutMilkshakes" />
      </div>

      <div v-if="!hiddenActivity">
        <ChoiceLogic :choices="allDecks.activityDeck" />
      </div>

      <div id="deckContainer" :class="{hiddenContainer: hiddenContainer}" class="deck-grid">
        <button
          v-for="(deck, key) in allDecks"
          :key="`${deck}${key}`"
          class="deckButton"
          @click="sendKey(key)"
          :class="{ hiddenDick: hiddenDeck }"
        >
          <div class="deck-container">
            <h2 class="deckTitle">{{deck.title}}</h2>
            <div class="overlay">
              <img class="deckImage" :src="deck.image" :alt="deck.description" />
            </div>
          </div>
        </button>
      </div>
    </div>
    <div>
      <footer v-if="!hiddenDeck" class="footer" role="contentinfo"></footer>
      <footer v-if="hiddenDeck" class="choice-footer" role="contentinfo"></footer>
    </div>
  </section>
</template>


<script>
import ChoiceLogic from "./ChoiceLogic";

import axios from "axios";

const yelpBaseURL =
  "https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?";
const yelpApiKey =
  "SM6pJx7LlCeKgElTpKU3PgsBDvqZud92PBBhqRBOEunqL9az6MmnAN9GUf4_mjjQva10STsyAlOs6RacEdskjV3qx7X_SjhqtpFVY0G0KzKvDoXcb4s-X2eZHOc5XXYx";
const databaseBaseURL = "//decidor.herokuapp.com/starterdecks/";

const bookBaseURL = `https://api.nytimes.com/svc/books/v3/lists/current/`;
const nytApiKey = `4QC7YMXjnIWo1dTtGFpj5itZlVDPvbOk`;

// const movieBaseURL =
//   "https://api.internationalshowtimes.com/v4/movies/?fields=title,slug,website,poster_image.flat&countries=US&release_date_to=";
// const movieApiKey = "LafOf9zLcvERnGpF3IBU85w8txyALDvH";

// const movieCityURL =
//   "https://api.internationalshowtimes.com/v4/cities/?countries=US&";

export default {
  name: "Decks",
  components: {
    ChoiceLogic
  },
  data: () => {
    return {
      allDecks: {
        // inTheaters: [],
        netflixDeck: [],
        netflixFilmsDeck: [],
        fictionDeck: [],
        nonFictionDeck: [],
        yelpRestaurants: [],
        foodTypesDeck: [],
        fastFoodDeck: [],
        cookoutMilkshakes: [],
        yelpArts: [],
        yelpShops: [],
        yelpParks: [],
        custom: [],
        activityDeck: []
      },
      database: [],
      // hiddenCards: true,
      cityName: "",
      searchingFor: "",
      book_category: "",
      searchTerm: "",
      hiddenDeck: false,
      hiddenTitle: false,
      hiddenContainer: false,
      businesses: [],
      results: [],
      // movies: [],
      // cities: [],
      // cityID: "",
      // movieLocation: "",
      hiddenBusiness: true,
      hiddenNetflix: true,
      hiddenFood: true,
      hiddenActivity: true,
      hiddenFoodTypes: true,
      hiddenFictionBooks: true,
      hiddenNonFictionBooks: true,
      hiddenSearch: true,
      hiddenCustomSearch: true,
      // hiddenMovieSearch: true,
      hiddenNav: false,
      hiddenMilkshakes: true,
      // hiddenMovies: true,
      hiddenNetflixFilms: true,
      formattedSearch: "",
      lat: "",
      lon: "",
      inputFilled: false
    };
  },
  mounted() {
    this.buildLocalApi();
    // this.allDecks.inTheaters.title = "In Theaters Now";
    // this.allDecks.inTheaters.image =
    //   "//decidor.s3.amazonaws.com/toy_story.jpeg";
    // this.allDecks.inTheaters.description =
    //   "A collection of movies currently in theaters";
    this.allDecks.netflixDeck.title = "Netflix Shows";
    this.allDecks.netflixDeck.image =
      "//decidor.s3.amazonaws.com/netflix_logo.jpeg";
    this.allDecks.netflixDeck.description =
      "A collection of popular Netflix Original Series";
    this.allDecks.netflixFilmsDeck.title = "Netflix Films";
    this.allDecks.netflixFilmsDeck.image =
      "//decidor.s3.amazonaws.com/netflix_white.png";
    this.allDecks.netflixFilmsDeck.description =
      "A collection of popular Netflix Original Films";
        this.allDecks.fictionDeck.title = "Fiction";
    this.allDecks.fictionDeck.image =
      "//decidor.s3.amazonaws.com/NYT_yellow_square.png";
    this.allDecks.fictionDeck.description =
      "A collection of the New York Times most recent Hardcover Fiction BestSelling Books";
    this.allDecks.nonFictionDeck.title = "Non-Fiction";
    this.allDecks.nonFictionDeck.image =
      "//decidor.s3.amazonaws.com/NYT_blue_square.png";
    this.allDecks.nonFictionDeck.description =
      "A collection of the New York Times most recent Hardcover Non-Fiction BestSelling Books";
    this.allDecks.yelpRestaurants.title = "Restaurants";
    this.allDecks.yelpRestaurants.image =
      "//decidor.s3.amazonaws.com/restaurants.jpeg";
    this.allDecks.yelpRestaurants.description =
      "A collection of restaurants near your location";
    this.allDecks.foodTypesDeck.title = "Types of Cuisine";
    this.allDecks.foodTypesDeck.image =
      "//decidor.s3.amazonaws.com/foodtypes.jpeg";
    this.allDecks.foodTypesDeck.description =
      "A collection of various regional and ethnic cuisines";
    this.allDecks.fastFoodDeck.title = "Fast Food";
    this.allDecks.fastFoodDeck.image =
      "//decidor.s3.amazonaws.com/national-french-fry-day.jpg";
    this.allDecks.fastFoodDeck.description =
      "A collection of popular US fast food and fast casual chain resturants";
    this.allDecks.cookoutMilkshakes.title = "Milkshakes";
    this.allDecks.cookoutMilkshakes.image =
      "//decidor.s3.amazonaws.com/cookoutmilkshake.jpeg";
    this.allDecks.cookoutMilkshakes.description =
      "A complete collection of all the flavors of milkshake available at the Southern US chain restaurant Cook Out";
    this.allDecks.yelpArts.title = "Attractions";
    this.allDecks.yelpArts.image = "//decidor.s3.amazonaws.com/arts.jpeg";
    this.allDecks.yelpArts.description =
      "A collection of attractions and local hotspots near your location";
    this.allDecks.yelpShops.title = "Shops";
    this.allDecks.yelpShops.image = "//decidor.s3.amazonaws.com/shops.jpeg";
    this.allDecks.yelpShops.description =
      "A collection of shops near your location";
    this.allDecks.yelpParks.title = "Parks";
    this.allDecks.yelpParks.image = "//decidor.s3.amazonaws.com/parks.jpeg";
    this.allDecks.yelpParks.description =
      "A collection of public parks, skate parks, and dog parks near your location";
    this.allDecks.custom.title = "Custom Search";
    this.allDecks.custom.image = "//decidor.s3.amazonaws.com/custom.jpeg";
    this.allDecks.custom.description =
      "A collection that you can create using your own search term and location";
        this.allDecks.activityDeck.title = "Date Night";
    this.allDecks.activityDeck.image =
      "//decidor.s3.amazonaws.com/couple-popcorn-movies.jpg";
    this.allDecks.activityDeck.description =
      "A collection of activities for couples on a date";
  },
  methods: {
    sendKey(key) {
      this.getCardsOnClick(key);
      this.getSearchParam(key);
      this.getBookCategory(key);
    },
    getCardsOnClick(key) {
      this.hiddenDeck = true;
      this.hiddenTitle = true;
      this.hiddenContainer = true;
      this.hiddenNav = true;
      if (key.includes("netflixDeck")) {
        this.hiddenNetflix = false;
      } else if (key.includes("fastFoodDeck")) {
        this.hiddenFood = false;
      } else if (key.includes("activityDeck")) {
        this.hiddenActivity = false;
      } else if (key.includes("foodTypesDeck")) {
        this.hiddenFoodTypes = false;
      } else if (key.includes("cookoutMilkshakes")) {
        this.hiddenMilkshakes = false;
      } else if (key.includes("netflixFilmsDeck")) {
        this.hiddenNetflixFilms = false;
      } else if (key.includes("yelp")) {
        this.hiddenSearch = false;
      } else if (key.includes("custom")) {
        this.hiddenCustomSearch = false;
        // } else if (key.includes("inTheaters")) {
        //   this.hiddenMovieSearch = false;
      }
    },
    getLocation: function() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.showPosition);
      } else {
        this.error = "Geolocation is not supported.";
      }
    },
    showPosition: function(position) {
      this.lat = position.coords.latitude;
      this.lon = position.coords.longitude;
      this.getLatLonBusinesses();
    },
    getSearchParam(key) {
      if (key.includes("yelpRestaurants")) {
        this.searchingFor = "categories=restaurants";
      } else if (key.includes("yelpShops")) {
        this.searchingFor = "categories=shopping,all";
      } else if (key.includes("yelpArts")) {
        this.searchingFor = "categories=arts,aquariums,localflavor";
      } else if (key.includes("yelpParks")) {
        this.searchingFor = "categories=parks,dog_parks,skate_parks";
      }
    },
    buildLatLonURL(url, searchingfor, lat, lon) {
      return `${yelpBaseURL}${this.searchingFor}&latitude=${this.lat}&longitude=${this.lon}`;
    },
    buildYelpURL(url, searchingFor, location) {
      return `${yelpBaseURL}${this.searchingFor}&location=${this.cityName}`;
    },
    getLatLonBusinesses() {
      if (!this.hiddenCustomSearch) {
        this.formattedSearch = this.searchTerm;
        this.formattedSearch = this.formattedSearch.replace(" ", "+");
        this.searchingFor = `term=${this.formattedSearch}`;
      }

      let apiURL = this.buildLatLonURL(
        yelpBaseURL,
        this.searchingFor,
        this.lat,
        this.lon
      );

      axios
        .get(apiURL, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            Authorization: `Bearer ${yelpApiKey}`
          }
        })
        .then(response => {
          this.allDecks.businesses = response.data.businesses;
          this.filterBusinesses(this.allDecks.businesses);
          this.hiddenBusiness = false;
        })
        .catch(error => {});
    },
    getBusinesses() {
      if (!this.hiddenCustomSearch) {
        this.formattedSearch = this.searchTerm;
        this.formattedSearch = this.formattedSearch.replace(" ", "+");
        this.searchingFor = `term=${this.formattedSearch}`;
      }

      let apiURL = this.buildYelpURL(
        yelpBaseURL,
        this.searchingFor,
        this.cityName
      );

      axios
        .get(apiURL, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            Authorization: `Bearer ${yelpApiKey}`
          }
        })
        .then(response => {
          this.allDecks.businesses = response.data.businesses;
          console.log(response.data.businesses);
          this.filterBusinesses(this.allDecks.businesses);
          this.hiddenBusiness = false;
        })
        .catch(error => {});
    },
    filterBusinesses() {
      let filteredBusinesses = this.allDecks.businesses.filter(
        business => business.image_url !== ""
      );
      filteredBusinesses.map(business => {
        let businessName = business.name;
        let businessImageURL = business.image_url;
        // let businessRating = business.rating;
        let businessURL = business.url;

        this.allDecks.yelpRestaurants.push({
          title: businessName,
          card_image: businessImageURL,
          // rating: businessRating,
          url: businessURL
        });
        filteredBusinesses = [];
        this.allDecks.businesses = [];
        this.hiddenSearch = true;
        this.hiddenCustomSearch = true;
        return this.allDecks.yelpRestaurants;
      });
    },
    getBookCategory(key) {
      if (key.includes("fictionDeck")) {
        this.book_category = "hardcover-fiction";
        this.getFictionBookList(key);
      }
      if (key.includes("nonFictionDeck")) {
        this.book_category = "hardcover-nonfiction";
        this.getNonFictionBookList(key);
      }
    },
    buildBookURL(bookBaseURL, book_category, nytApiKey) {
      return `${bookBaseURL}${this.book_category}.json?api-key=${nytApiKey}`;
    },
    getFictionBookList(key) {
      let bookApiURL = this.buildBookURL(
        bookBaseURL,
        this.book_category,
        nytApiKey
      );

      axios
        .get(bookApiURL)
        .then(response => {
          this.results = response.data.results;
          this.hiddenFictionBooks = false;
          this.filterFictionBooks(this.results);
        })
        .catch(error => {});
    },
    filterFictionBooks() {
      this.results.books.map(book => {
        let bookTitle = book.title;
        let bookAuthor = book.author;
        let bookDescription = book.description;
        let bookCover = book.book_image;
        let bookURL = book.amazon_product_url;

        this.allDecks.fictionDeck.push({
          title: bookTitle,
          description: bookDescription,
          card_image: bookCover,
          url: bookURL
        });
        this.results = [];
        return this.allDecks.fictionDeck;
      });
    },
    getNonFictionBookList(key) {
      let bookApiURL = this.buildBookURL(
        bookBaseURL,
        this.book_category,
        nytApiKey
      );

      axios
        .get(bookApiURL)
        .then(response => {
          this.results = response.data.results;
          this.hiddenNonFictionBooks = false;
          this.filterNonFictionBooks(this.results);
        })
        .catch(error => {});
    },
    filterNonFictionBooks() {
      this.results.books.map(book => {
        let bookTitle = book.title;
        let bookAuthor = book.author;
        let bookDescription = book.description;
        let bookCover = book.book_image;
        let bookURL = book.amazon_product_url;

        this.allDecks.nonFictionDeck.push({
          title: bookTitle,
          description: bookDescription,
          card_image: bookCover,
          url: bookURL
        });
        this.results = [];
        return this.allDecks.nonFictionDeck;
      });
    },
    // getCityID() {
    //   let completeCityURL = movieCityURL + "query=" + this.cityName;

    //   axios
    //     .get(completeCityURL, {
    //       headers: {
    //         Authorization: `Token ${movieApiKey}`
    //       }
    //     })
    //     .then(response => {
    //       this.cities = response.data.cities;
    //       this.cityID = this.cities[0].id;
    //       this.makeMovieCityURL();
    //     })
    //     .catch(error => {
    //       console.log(error);
    //     });
    // },
    // getMovieLocation: function() {
    //   if (navigator.geolocation) {
    //     navigator.geolocation.getCurrentPosition(this.showMoviePosition);
    //   } else {
    //     this.error = "Geolocation is not supported.";
    //   }
    // },
    // showMoviePosition: function(position) {
    //   this.lat = position.coords.latitude;
    //   this.lon = position.coords.longitude;
    //   this.makeMovieLatLonURL();
    // },
    // makeMovieLatLonURL(url) {
    //   this.movieLocation = `&location=${this.lat},${this.lon}&distance=30`;
    //   this.getMovies();
    // },
    // makeMovieCityURL() {
    //   this.movieLocation = `&city_ids=${this.cityID}`;
    //   this.getMovies();
    // },
    // getMovies() {
    //   let todaysDate = new Date();
    //   let month = ("0" + (todaysDate.getMonth() + 1)).slice(-2);
    //   let date = ("0" + todaysDate.getDate()).slice(-2);
    //   let year = todaysDate.getFullYear();
    //   let formattedDate = year + "-" + month + "-" + date;

    //   let startDate = new Date();
    //   let sDate = ("0" + startDate.getDate()).slice(-2);
    //   let sMonth = ("0" + (startDate.getMonth() - 1)).slice(-2);
    //   let sYear = startDate.getFullYear();
    //   let twoMonthsAgoDate = sYear + "-" + sMonth + "-" + sDate;

    //   let movieApiURL = `${movieBaseURL}${formattedDate}&release_date_from=${twoMonthsAgoDate}`;
    //   movieApiURL = movieApiURL + this.movieLocation;

    //   axios
    //     .get(movieApiURL, {
    //       headers: {
    //         Authorization: `Token ${movieApiKey}`
    //       }
    //     })
    //     .then(response => {
    //       this.allDecks.movies = response.data.movies;
    //       console.log(response.data.movies);
    //       this.filterMovies(this.allDecks.movies);
    //       this.hiddenMovies = false;
    //       this.hiddenMovieSearch = true;
    //     })
    //     .catch(error => {
    //       console.log(error);
    //     });
    // },
    // filterMovies() {
    //   let filteredMovies = this.allDecks.movies.filter(
    //     movie => movie.poster_image !== null
    //   );
    //   filteredMovies.map(movie => {
    //     let movieTitle = movie.title;
    //     let movieDescription = movie.slug;
    //     let movieCover = movie.poster_image;
    //     let movieURL = movie.website;

    //     this.allDecks.inTheaters.push({
    //       title: movieTitle,
    //       description: movieDescription,
    //       card_image: movieCover,
    //       url: movieURL
    //     });
    //     filteredMovies = [];
    //     this.allDecks.movies = [];
    //     return this.allDecks.inTheaters;
    //   });
    // },
    buildLocalApi() {
      axios.get(databaseBaseURL).then(response => {
        this.database = response.data.results;
        this.makeNetflixDeck(this.database);
        this.makeFastFoodDeck(this.database);
        this.makeActivityDeck(this.database);
        this.makeFoodTypesDeck(this.database);
        this.makeCookoutMilkshakesDeck(this.database);
        this.makeNetflixFilmsDeck(this.database);
      });
    },

    makeNetflixDeck() {
      this.database[0].card_set.map(card => {
        let cardTitle = card.title;
        let cardImage = card.card_image;
        let cardDeck = card.deck;
        let cardDescription = card.description;
        let cardURL = card.url;

        this.allDecks.netflixDeck.push({
          title: cardTitle,
          card_image: cardImage,
          description: cardDescription,
          url: cardURL
        });
        return this.allDecks.netflixDeck;
      });
    },
    makeFastFoodDeck() {
      this.database[2].card_set.map(card => {
        let cardTitle = card.title;
        let cardImage = card.card_image;
        let cardDeck = card.deck;
        let cardDescription = card.description;
        let cardURL = card.url;

        this.allDecks.fastFoodDeck.push({
          title: cardTitle,
          card_image: cardImage,
          description: cardDescription,
          url: cardURL
        });
        return this.allDecks.fastFoodDeck;
      });
    },
    makeActivityDeck() {
      this.database[3].card_set.map(card => {
        let cardTitle = card.title;
        let cardImage = card.card_image;
        let cardDeck = card.deck;
        let cardDescription = card.description;
        let cardURL = card.url;

        this.allDecks.activityDeck.push({
          title: cardTitle,
          card_image: cardImage,
          description: cardDescription,
          url: cardURL
        });
        return this.allDecks.activityDeck;
      });
    },
    makeFoodTypesDeck() {
      this.database[4].card_set.map(card => {
        let cardTitle = card.title;
        let cardImage = card.card_image;
        let cardDeck = card.deck;
        let cardDescription = card.description;
        let cardURL = card.url;

        this.allDecks.foodTypesDeck.push({
          title: cardTitle,
          card_image: cardImage,
          description: cardDescription,
          url: cardURL
        });
        return this.allDecks.foodTypesDeck;
      });
    },
    makeCookoutMilkshakesDeck() {
      this.database[5].card_set.map(card => {
        let cardTitle = card.title;
        let cardImage = card.card_image;
        let cardDeck = card.deck;
        let cardDescription = card.description;
        let cardURL = card.url;

        this.allDecks.cookoutMilkshakes.push({
          title: cardTitle,
          card_image: cardImage,
          description: cardDescription,
          url: cardURL
        });
        return this.allDecks.cookoutMilkshakes;
      });
    },
    makeNetflixFilmsDeck() {
      this.database[1].card_set.map(card => {
        let cardTitle = card.title;
        let cardImage = card.card_image;
        let cardDeck = card.deck;
        let cardDescription = card.description;
        let cardURL = card.url;

        this.allDecks.netflixFilmsDeck.push({
          title: cardTitle,
          card_image: cardImage,
          description: cardDescription,
          url: cardURL
        });
        return this.allDecks.netflixFilmsDeck;
      });
    }
  }
};
</script>