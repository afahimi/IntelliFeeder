<template>
  <div class="q-pa-md">

    <!-- toggle between cat and dog settings tabs -->
    <div style="max-width: 600px">
      <q-tabs v-model="tab" align="justify" narrow-indicator class="q-mb-lg">
        <q-tab class="text-blue" name="Dog" label="Dog" />
        <q-tab class="text-blue" name="Cat" label="Cat" />
      </q-tabs>

      <!-- cat and dog settings tabs -->
      <div class="q-gutter-y-sm">
        <q-tab-panels v-model="tab" animated transition-prev="scale" transition-next="scale"
          class="bg-white text-primary text-center" style="border-radius: 20px;">
          <q-tab-panel name="Dog">
            <div class="text-h6">Dog</div>
            <div class="q-pa-lg">
              <label class="text-h6">Number of servings per day</label> <!-- q-slider component for the number of servings per day -->
              <q-slider v-model="dogNumServings" color="primary" thumb-color="primary" markers marker-labels
                marker-labels-class="text-black" switch-marker-labels-side switch-label-side :min="1" :max="4" />
            </div>
            <div class="q-pa-md">
              <q-row>
                <q-col v-for="i in dogNumServings" :key="i"> <!-- q-input component for the time of each serving -->
                  <q-input filled v-model="dogTimes[i - 1]" mask="time" :rules="['time']">
                    <template v-slot:append>
                      <q-icon name="access_time" class="cursor-pointer">
                        <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                          <q-time v-model="dogTimes[i - 1]" :hour="12" :minute="0">
                            <div class="row items-center justify-end">
                              <q-btn v-close-popup label="Close" color="primary" flat />
                            </div>
                          </q-time>
                        </q-popup-proxy>
                      </q-icon>
                    </template>
                  </q-input>
                </q-col>
              </q-row>
            </div>
            <label style="padding-left: 5%" class="text-h6">Portion Sizes</label>
            <div class="q-pa-md"> <!-- q-btn-toggle component for the portion sizes -->
              <q-btn-toggle v-model="dogPortionSize" toggle-color="primary" :options="[
                { label: 'Small', value: 1 },
                { label: 'Medium', value: 2 },
                { label: 'Large', value: 3 },
              ]" @click.native="toggleDogStyle" :class="{ toggled: dogToggled }" />
            </div>
          </q-tab-panel>

          <q-tab-panel name="Cat">
            <div class="text-h6">Cat</div>
            <div class="q-pa-lg"> <!-- q-slider component for the number of servings per day -->
              <label class="text-h6">Number of servings per day</label>
              <q-slider v-model="catNumServings" color="primary" thumb-color="primary" markers marker-labels
                marker-labels-class="text-black" switch-marker-labels-side switch-label-side :min="1" :max="4" />
            </div>

            <div class="q-pa-md">
              <q-row> <!-- q-input component for the time of each serving -->
                <q-col v-for="i in catNumServings" :key="i" cols="12">
                  <q-input filled v-model="catTimes[i - 1]" mask="time" :rules="['time']">
                    <template v-slot:append>
                      <q-icon name="access_time" class="cursor-pointer">
                        <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                          <q-time v-model="catTimes[i - 1]" :hour="12" :minute="0">
                            <div class="row items-center justify-end">
                              <q-btn v-close-popup label="Close" color="primary" flat />
                            </div>
                          </q-time>
                        </q-popup-proxy>
                      </q-icon>
                    </template>
                  </q-input>
                </q-col>
              </q-row>
            </div>
            <label style="padding-left: 5%" class="text-h6">Portion Sizes</label>
            <div class="q-pa-md"> <!-- q-btn-toggle component for the portion sizes -->
              <q-btn-toggle v-model="catPortionSize" toggle-color="primary" :options="[
                { label: 'Small', value: 1 },
                { label: 'Medium', value: 2 },
                { label: 'Large', value: 3 },
              ]" @click.native="toggleCatStyle" :class="{ toggled: catToggled }" />
            </div>
          </q-tab-panel>
        </q-tab-panels>
      </div>
    </div>
    <div class = "q-pa-md">
      <q-ajax-bar
      ref="bar"
      position="bottom"
      color="primary"
      size="10px"
      skip-hijack
    /> <!-- ajax bar component to show progress of sending data to server with apply settings button -->
      <q-btn @click = "collectDataAndSend(); trigger()"  rounded unelevated
      :disable="disableButton"
      class = "apply-btn"
      size="20px" label="Apply"
      />
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  setup() {

    // ajax bar function to show progress of sending data to server with apply settings button
    const bar = ref(null)
    function trigger () {
      const barRef = bar.value
      barRef.start()
      setTimeout(() => {
        const barRef = bar.value
        if (barRef) {
          barRef.stop()
        }
      }, Math.random() * 400 + 10)
    }
    return {
      bar,
      trigger,
      tab: ref("Dog"),

    };
  },
  data() {
    return {
      // Initializing data for the dog and cat tabs at load up
      tab: 'Dog',
      dogNumServings: 1,
      dogTimes: ['0000', '0000', '0000', '0000'],
      dogPortionSize: 1,
      dogToggled: false,
      catNumServings: 1,
      catTimes: ['0000', '0000', '0000', '0000'],
      catPortionSize: 1,
      catToggled: false,
    }
  },
  //Converting the time strings to seconds from current time to send to server
  computed: {
    dogTimesInSeconds() {
      return this.dogTimes.map(timeString => this.secondsFromCurrentTime(timeString));
    },
    catTimesInSeconds() {
      return this.catTimes.map(timeString => this.secondsFromCurrentTime(timeString));
    },
    //Disabling the apply button if the time is not in the correct format
    disableButton() {
      const regex = /^([01]\d|2[0-3]):?([0-5]\d)$/;
      for (let i = 0; i < this.dogTimes.length; i++) {
        if (!regex.test(this.dogTimes[i])) {
          return true;
        }
      }
      for (let i = 0; i < this.catTimes.length; i++) {
        if (!regex.test(this.catTimes[i])) {
          return true;
        }
      }
      return false;
    }
  },

  methods: {
    //Converting the time strings to seconds from current time to send to server
    secondsFromCurrentTime(timeString) {
      const currentTime = new Date();
      const [hours, minutes] = timeString.split(":");
      const targetTime = new Date(
        currentTime.getFullYear(),
        currentTime.getMonth(),
        currentTime.getDate(),
        hours,
        minutes
      );
      const timeDifference = targetTime.getTime() - currentTime.getTime();
      return Math.floor(timeDifference / 1000);
    },
    toggleDogStyle() {
      this.dogToggled = !this.dogToggled
    },
    toggleCatStyle() {
      this.catToggled = !this.catToggled
    },
    showDogServings() {
      alert(`Number of dog servings: ${this.dogNumServings}`)
    },
    //Sending the data to the server
    async collectDataAndSend() {
      const data = {
        request: 'feed-data',
        Dog: {
          numServings: this.dogNumServings,
          times: this.dogTimesInSeconds,
          portionSize: this.dogPortionSize
        },
        Cat: {
          numServings: this.catNumServings,
          times: this.catTimesInSeconds,
          portionSize: this.catPortionSize
        }
      }
      const jsonData = JSON.stringify(data)
      console.log(jsonData)

      try {
        const response = await fetch("http://localhost:5000/api/feed", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: jsonData
        })

        const responseData = await response.json()
        console.log(responseData)
      } catch (error) {
        console.error(error)
      }
    }

  },
  //Adding more time inputs if the user wants to add more servings
  watch: {
    dogNumServings(val) {
      const times = []
      for (let i = 0; i < val; i++) {
        if (i < this.dogTimes.length) {
          times.push(this.dogTimes[i])
        } else {
          times.push('0000')
        }
      }
      this.dogTimes = times
    },
    catNumServings(val) {
      const times = []
      for (let i = 0; i < val; i++) {
        if (i < this.catTimes.length) {
          times.push(this.catTimes[i])
              }
              else {
          times.push('0000')
        }
      }
      this.catTimes = times
    },
  },
};
</script>

<style lang="scss">
.apply-btn {
  padding-top: 20px;
  padding-bottom: 20px;
  border: 6px solid rgba(255,255,255, 0.9);
  border-radius: 50px;
  //background-image: linear-gradient(90deg, #0061ff, #60efff);
  background-image:  linear-gradient(-45deg, #6f7bf7, #12cff3, #338AFF, #30c5d2);
  animation: anime 14s linear infinite;
  background-repeat: no-repeat;
  background-clip: padding-box;
  width: 100%;
  color: white;
  background-size: 600%;
}
//Animation for the apply button
@keyframes anime {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

</style>
