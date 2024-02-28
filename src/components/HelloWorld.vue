<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)

import { post, get } from 'aws-amplify/api';

async function postTodo() {
  try {
    const restOperation = get({
      apiName: 'flaskvueapi',
      path: '/items'
    });

    const { body } = await restOperation.response;
    const response = await body.json();

    console.log('POST call succeeded');
    console.log(response);
  } catch (e) {
    console.log('POST call failed: ', e);
  }
}


</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="postTodo()">count is {{ count }}</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/vuejs/language-tools" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
