<template>
  <div class="q-pa-md">
    <div style="max-width: 600px">
      <q-btn @click="collectDataAndSend" :disable="disableButton">Apply</q-btn>

      <q-tabs v-model="tab" align="justify" narrow-indicator class="q-mb-lg">
        <q-tab class="text-blue" name="Dog" label="Dog" />
        <q-tab class="text-blue" name="Cat" label="Cat" />
      </q-tabs>

      <div class="q-gutter-y-sm">
        <q-tab-panels v-model="tab" animated transition-prev="scale" transition-next="scale"
          class="bg-white text-primary text-center">
          <q-tab-panel name="Dog">
            <div class="text-h6">Dog</div>
            <div class="q-pa-lg">
              <label class="text-h6">Number of servings per day</label>
              <q-slider v-model="dogNumServings" color="primary" thumb-color="primary" markers marker-labels
                marker-labels-class="text-black" switch-marker-labels-side switch-label-side :min="1" :max="4" />
            </div>
            <div class="q-pa-md">
              <q-row>
                <q-col v-for="i in dogNumServings" :key="i">
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
            <div class="q-pa-md">
              <q-btn-toggle v-model="dogPortionSize" toggle-color="primary" :options="[
                { label: 'Small', value: 'one' },
                { label: 'Medium', value: 'two' },
                { label: 'Large', value: 'three' },
              ]" @click.native="toggleDogStyle" :class="{ toggled: dogToggled }" />
            </div>
          </q-tab-panel>

          <q-tab-panel name="Cat">
            <div class="text-h6">Cat</div>
            <div class="q-pa-lg">
              <label class="text-h6">Number of servings per day</label>
              <q-slider v-model="catNumServings" color="primary" thumb-color="primary" markers marker-labels
                marker-labels-class="text-black" switch-marker-labels-side switch-label-side :min="1" :max="4" />
            </div>

            <div class="q-pa-md">
              <q-row>
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
            <div class="q-pa-md">
              <q-btn-toggle v-model="catPortionSize" toggle-color="primary" :options="[
                { label: 'Small', value: 'one' },
                { label: 'Medium', value: 'two' },
                { label: 'Large', value: 'three' },
              ]" @click.native="toggleCatStyle" :class="{ toggled: catToggled }" />
            </div>
          </q-tab-panel>
        </q-tab-panels>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  setup() {
    return {
      tab: ref("Dog"),
    };
  },
  data() {
    return {
      tab: 'Dog',
      dogNumServings: 1,
      dogTimes: ['0000', '0000', '0000', '0000'],
      dogPortionSize: 'one',
      dogToggled: false,
      catNumServings: 1,
      catTimes: ['0000', '0000', '0000', '0000'],
      catPortionSize: 'one',
      catToggled: false,
    }
  },
  computed: {
    dogTimesInSeconds() {
      return this.dogTimes.map(timeString => this.secondsFromCurrentTime(timeString));
    },
    catTimesInSeconds() {
      return this.catTimes.map(timeString => this.secondsFromCurrentTime(timeString));
    },
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
  watch: {
    dogNumServings(val) {
      const times = []
      for (let i = 0; i < val; i++) {
        if (i < this.dogTimes.length) {
          times.push(this.dogTimes[i])
        } else {
          times.push('')
        }
      }
      this.dogTimes = times
    },
    catNumServings(val) {
      const times = []
      for (let i = 0; i < val; i++) {
        if (i < this.catTimes.length) {
          times.push(this.catTimes[i])
        } else {
          times.push('')
        }
      }
      this.catTimes = times
    },
  },
};
</script>
