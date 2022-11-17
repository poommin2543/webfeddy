<template>
  <div class='hello'>
    <div>
      <input type="text" v-model="name" placeholder="NAME">
      <input type="text" v-model="tel" placeholder="TEL">
      <button @click="insertToContact(tel, name)">Add</button>
    </div>

    <hr>

    <ul :key="key" v-for="(contact, key) in contacts">
      <li v-if="updateKey === key">
        <input type="text" v-model="updateName" placeholder="NAME">
        <input type="text" v-model="updateTel" placeholder="TEL">
        <button @click="updateContact(updateTel, updateName)">Save</button>
      </li>
      <li v-else>
        {{contact.name}} : {{contact.tel}} 
        <button @click="setUpdateContact(key, contact)">Update</button>
        <button @click="deleteContact(key)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
import * as firebase from '@/components/firebase'
var config = {
  
  apiKey: "AIzaSyB9RkZFAwtJfZUXYvXZBb2S4GYVSzOkpjE",
  authDomain: "location-a26be.firebaseapp.com",
  databaseURL: "https://location-a26be-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "location-a26be",
  storageBucket: "location-a26be.appspot.com",
  messagingSenderId: "275944322136",
  appId: "1:275944322136:web:70f14965096c7dff1e462d",
  measurementId: "G-2W7W0Z25Y4"
}
firebase.initializeApp(config)
var database = firebase.database()
var contactRef = database.ref('/contacts')
export default {
  name: 'HelloWorld',
  data () {
    return {
      contacts: {},
      tel: '',
      name: '',
      updateTel: '',
      updateName: '',
      updateKey: ''
    }
  },
  methods: {
    insertToContact (tel, name) {
      let data = {
        tel: tel,
        name: name
      }
      contactRef.push(data)
      this.tel = ''
      this.name = ''
    },
    setUpdateContact (key, contact) {
      this.updateKey = key
      this.updateTel = contact.tel
      this.updateName = contact.name
    },
    updateContact (tel, name) {
      contactRef.child(this.updateKey).update({
        tel: tel,
        name: name
      })
      this.updateKey = ''
      this.updateTel = ''
      this.updateName = ''
    },
    deleteContact (key) {
      contactRef.child(key).remove()
    }
  },
  mounted () {
    contactRef.on('value', (snapshot) => {
      this.contacts = snapshot.val()
    })
  }
}
</script>

<!-- Add 'scoped' attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>