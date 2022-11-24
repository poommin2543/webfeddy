(function(){"use strict";var e={3804:function(e,t,n){n(6992),n(8674),n(9601),n(7727);var r=n(8935),o=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("h1",[e._v("iPOND WebRTC Studio")]),n("h3",[e._v("Using Janus webRTC server.")]),n("div",{staticClass:"select-ctn"},[n("select",{directives:[{name:"model",rawName:"v-model",value:e.streamList.selected,expression:"streamList.selected"}],attrs:{disabled:e.stream},on:{change:function(t){var n=Array.prototype.filter.call(t.target.options,(function(e){return e.selected})).map((function(e){var t="_value"in e?e._value:e.value;return t}));e.$set(e.streamList,"selected",t.target.multiple?n:n[0])}}},e._l(e.streamList.options,(function(t){return n("option",{key:t.id,domProps:{value:t.id}},[e._v(" "+e._s(t.description)+" ")])})),0),n("div",[e._v(e._s(null==e.stream?"null":e.notNull))]),n("button",{attrs:{disabled:e.stream},on:{click:function(t){return t.preventDefault(),e.start.apply(null,arguments)}}},[e._v("Start")]),n("button",{attrs:{disabled:!e.stream},on:{click:function(t){return t.preventDefault(),e.stop.apply(null,arguments)}}},[e._v("Stop")])]),"starting"==e.status?n("h3",[e._v(" Loading video stream ... ")]):e._e(),n("div",{staticClass:"video-vtn"},[n("video",{ref:"videoStream",attrs:{autoplay:"autoplay",playsinline:"",width:"640px",height:"480px"},domProps:{srcObject:e.stream}})]),e.stream?e._e():n("div",[e._v("No Stream")]),n("div",[e._v("Status: "+e._s(e.status?e.status:"No video stream"))]),e.error?n("div",[e._v(e._s(e.error))]):e._e()])},s=[],i=(n(4916),n(5306),n(9828)),a="http://34.143.225.243:8088/janus",u={name:"App",data:function(){return{janus:null,error:null,plugin:null,status:null,stream:null,streamList:{selected:null,options:[]},remoteTracks:{},remoteVideos:0}},mounted:function(){var e=this;i.c.init({debug:!0,dependencies:i.c.useDefaultDependencies(),callback:function(){console.log("Connecting to Janus api with server ",a),e.connect(a)}})},methods:{connect:function(e){var t=this;this.janus=new i.c({server:e,success:function(){console.log("Connected"),t.attachPlugin()},error:function(e){console.log("Error"),t.onError("Failed to connect janus server",e)},destroyed:function(){console.log("Destroyed"),window.location.reload()}})},attachPlugin:function(){var e=this;this.janus.attach({plugin:"janus.plugin.streaming",opaqueId:"thisisopaqueid",success:function(t){e.plugin=t,console.log("getBitrate : ",e.plugin.getBitrate()),e.updateStreamsList()},error:function(t){e.onError("Error attaching plugin... ",t)},iceState:function(e){console.log("ICE state changed to ",e)},webrtcState:function(e){console.log("Janus says our WebRTC PeerConnection is "+(e?"up":"down")+" now")},slowLink:function(e,t,n){console.log("Janus reports problems "+(e?"sending":"receiving")+" packets on mid "+n+" ("+t+" lost packets)")},onmessage:function(t,n){console.log(" ::: Got a message :::",t);var r=t.result;if(r)r.status&&(e.status=r.status);else if(t.error)return e.onError(t.error),void e.stop();if(n){i.c.debug("Handling SDP as Well... ",n);var o=-1!==n.sdp.indexOf("stereo=1");e.plugin.createAnswer({jsep:n,media:{audioSend:!1,videoSend:!1,data:!0},customizeSdp:function(e){o&&-1==e.sdp.indexOf("stereo=1")&&(e.sdp=e.sdp.replace("useinbandfec=1","useinbandfec=1;stereo=1"))},success:function(t){i.c.debug("Got SDP!",t);var n={request:"start"};e.plugin.send({message:n,jsep:t})},error:function(t){e.onError("WebRTC Error: ",t),alert("WebRTC error... ",t)}})}},onremotetrack:function(t,n,r){i.c.debug("Remote track (mid="+n+") "+(r?"added":"removed")+":",t),"video"===t.kind&&(e.remoteVideos++,e.stream=new MediaStream,e.stream.addTrack(t.clone()),e.remoteTracks.mid=e.stream,i.c.log("Created remote audio stream:",e.stream))},oncleanup:function(){e.onCleanup()}})},updateStreamsList:function(){var e=this;this.plugin.send({message:{request:"list"},success:function(t){t||e.onError("Got no response to our query for available streams."),console.log("Updating StreamList....",t),e.streamList.options=t.list,t.list.length&&(e.streamList.selected=e.streamList.options[0].id)}})},start:function(){this.plugin.send({message:{request:"watch",id:this.streamList.selected}})},stop:function(){this.plugin.send({message:{request:"stop"}}),this.plugin.hangup()},onCleanup:function(){i.c.log(" ::: Got a cleanup notification :::"),this.stream=null,this.status=null,this.remoteTracks={},this.remoteVideos=0,this.error=null},onError:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"";i.c.error(e,t),this.error=e+t,alert(this.error,(function(){window.location.reload()}))}}},c=u,l=n(1001),d=(0,l.Z)(c,o,s,!1,null,null,null),f=d.exports;r.Z.config.productionTip=!1,new r.Z({render:function(e){return e(f)}}).$mount("#app")}},t={};function n(r){var o=t[r];if(void 0!==o)return o.exports;var s=t[r]={id:r,loaded:!1,exports:{}};return e[r](s,s.exports,n),s.loaded=!0,s.exports}n.m=e,function(){var e=[];n.O=function(t,r,o,s){if(!r){var i=1/0;for(l=0;l<e.length;l++){r=e[l][0],o=e[l][1],s=e[l][2];for(var a=!0,u=0;u<r.length;u++)(!1&s||i>=s)&&Object.keys(n.O).every((function(e){return n.O[e](r[u])}))?r.splice(u--,1):(a=!1,s<i&&(i=s));if(a){e.splice(l--,1);var c=o();void 0!==c&&(t=c)}}return t}s=s||0;for(var l=e.length;l>0&&e[l-1][2]>s;l--)e[l]=e[l-1];e[l]=[r,o,s]}}(),function(){n.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(t,{a:t}),t}}(),function(){n.d=function(e,t){for(var r in t)n.o(t,r)&&!n.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){n.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){n.nmd=function(e){return e.paths=[],e.children||(e.children=[]),e}}(),function(){var e={143:0};n.O.j=function(t){return 0===e[t]};var t=function(t,r){var o,s,i=r[0],a=r[1],u=r[2],c=0;if(i.some((function(t){return 0!==e[t]}))){for(o in a)n.o(a,o)&&(n.m[o]=a[o]);if(u)var l=u(n)}for(t&&t(r);c<i.length;c++)s=i[c],n.o(e,s)&&e[s]&&e[s][0](),e[s]=0;return n.O(l)},r=self["webpackChunkvue_janus"]=self["webpackChunkvue_janus"]||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))}();var r=n.O(void 0,[998],(function(){return n(3804)}));r=n.O(r)})();
//# sourceMappingURL=app-legacy.c136f7b8.js.map