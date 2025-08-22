// src/firebase.js
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyAVb1rH2-_xYAv4eJgc6y8OB96S2ddT4mw",
  authDomain: "eastusatours.firebaseapp.com",
  projectId: "eastusatours",
  storageBucket: "eastusatours.firebasestorage.app",
  messagingSenderId: "499773995286",
  appId: "1:499773995286:web:df782dd0127a733085f837",
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);

console.log("Firebase ready:", app.options.projectId);
