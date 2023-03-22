<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md">
      <div class="row">
        <div class="col col-md-auto q-pa-lg">
          <q-card class="history-card">
            <q-card-section>
              <div class="text-h6">Welcome to Feederdog</div>
            </q-card-section>
          </q-card>
        </div>
        <div class="col col-md-auto q-pa-lg">
          <div class="animal-container col justify-center">
            <div class="feeder-imgs justify-center">
              <q-carousel animated v-model="slide" arrows navigation infinite>
                <q-carousel-slide
                  :name="1"
                  img-src="https://cdn.quasar.dev/img/mountains.jpg"
                />
                <q-carousel-slide
                  :name="2"
                  img-src="https://cdn.quasar.dev/img/parallax1.jpg"
                />
                <q-carousel-slide
                  :name="3"
                  img-src="https://cdn.quasar.dev/img/parallax2.jpg"
                />
                <q-carousel-slide
                  :name="4"
                  img-src="https://cdn.quasar.dev/img/quasar.jpg"
                />
              </q-carousel>
            </div>
            <div class="justify-center flex q-pa-lg">
              <q-btn-toggle
                v-model="model"
                class="animal-toggle"
                no-caps
                rounded
                unelevated
                toggle-color="primary"
                color="white"
                text-color="primary"
                :options="[
                  { label: 'Auto', value: 'Auto' },
                  { label: 'Custom', value: 'Custom' },
                ]"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "IndexPage",
  setup() {
    return {
      slide: ref(1),
      model: ref("one"),
    };
  },
});
</script>

<style lang="scss">
.animal-toggle {
  border: 1px solid #027be3;
}
.history-card {
  width: 100%;
  text-align: center;
}
.animal-container {
  width: 400px;
}
</style>
