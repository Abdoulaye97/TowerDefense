(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[405],{8312:function(r,e,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/",function(){return n(1720)}])},4830:function(r,e,n){"use strict";n.d(e,{Z:function(){return b}});var t=n(4051),i=n.n(t),a=n(5893),o=n(3856),c=n(5675),s=n.n(c),l=n(8533);function u(r,e,n){return e in r?Object.defineProperty(r,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):r[e]=n,r}function d(r,e){if(null==r)return{};var n,t,i=function(r,e){if(null==r)return{};var n,t,i={},a=Object.keys(r);for(t=0;t<a.length;t++)n=a[t],e.indexOf(n)>=0||(i[n]=r[n]);return i}(r,e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(r);for(t=0;t<a.length;t++)n=a[t],e.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(r,n)&&(i[n]=r[n])}return i}var f=function(r){var e=r.width,n=(r.color,r.strokeWidth,r.className,r.children,d(r,["width","color","strokeWidth","className","children"])),t={};return e&&(t.width=e),(0,a.jsx)("div",function(r){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{},t=Object.keys(n);"function"===typeof Object.getOwnPropertySymbols&&(t=t.concat(Object.getOwnPropertySymbols(n).filter((function(r){return Object.getOwnPropertyDescriptor(n,r).enumerable})))),t.forEach((function(e){u(r,e,n[e])}))}return r}({className:"rtb-material-spinner",style:t},n,{children:(0,a.jsx)("svg",{className:"rtb-material-spinner-circular",viewBox:"25 25 50 50",children:(0,a.jsx)("circle",{className:"rtb-material-spinner-path",style:{},cx:"50",cy:"50",r:"20",fill:"none",strokeWidth:"2",strokeMiterlimit:"10"})})}))};function h(r,e){(null==e||e>r.length)&&(e=r.length);for(var n=0,t=new Array(e);n<e;n++)t[n]=r[n];return t}function p(r,e,n,t,i,a,o){try{var c=r[a](o),s=c.value}catch(l){return void n(l)}c.done?e(s):Promise.resolve(s).then(t,i)}function m(r){return function(){var e=this,n=arguments;return new Promise((function(t,i){var a=r.apply(e,n);function o(r){p(a,t,i,o,c,"next",r)}function c(r){p(a,t,i,o,c,"throw",r)}o(void 0)}))}}function g(r){return function(r){if(Array.isArray(r))return h(r)}(r)||function(r){if("undefined"!==typeof Symbol&&null!=r[Symbol.iterator]||null!=r["@@iterator"])return Array.from(r)}(r)||function(r,e){if(!r)return;if("string"===typeof r)return h(r,e);var n=Object.prototype.toString.call(r).slice(8,-1);"Object"===n&&r.constructor&&(n=r.constructor.name);if("Map"===n||"Set"===n)return Array.from(n);if("Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return h(r,e)}(r)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}var v=function(){var r=m(i().mark((function r(e){var n,t;return i().wrap((function(r){for(;;)switch(r.prev=r.next){case 0:return r.next=2,fetch(e);case 2:if((n=r.sent).ok){r.next=9;break}return t=new Error("An error occurred while fetching the data."),r.next=7,n.json();case 7:throw t.message=r.sent,t;case 9:return r.abrupt("return",n.json());case 10:case"end":return r.stop()}}),r)})));return function(e){return r.apply(this,arguments)}}();var b=function(r){var e,n=r.query,t=r.quotaUser,c=(0,o.ZP)((function(r,e){return e&&!e.length?null:"/api/search?query=".concat(n,"&page=").concat(10*r+1,"&qus=").concat(t)}),v,{initialSize:2,revalidateAll:!1,revalidateFirstPage:!1,persistSize:!1}),u=c.data,d=c.error,h=c.mutate,p=c.size,b=c.setSize,y=(c.isValidating,function(){var r=m(i().mark((function r(){return i().wrap((function(r){for(;;)switch(r.prev=r.next){case 0:return r.next=2,b(p+1);case 2:case"end":return r.stop()}}),r)})));return function(){return r.apply(this,arguments)}}()),j=u?(e=[]).concat.apply(e,g(u)):[],x=!u&&!d||p>0&&u&&"undefined"===typeof u[p-1],w=0===(null===u||void 0===u?void 0:u[0].length),k=!(w||u&&u[u.length-1].length<10)&&u&&u.length<2;if(d)return(0,a.jsxs)("div",{className:"grid-error cs1 ce12",children:[(0,a.jsx)("span",{className:"label label-warning",children:"error"}),(0,a.jsx)("br",{}),(0,a.jsx)("br",{}),(0,a.jsx)("p",{className:"p-small",children:"An error occurred while loading. Please try again or contact support if the issue persists."}),(0,a.jsx)("br",{}),(0,a.jsx)("div",{className:"button button-secondary",onClick:function(){return h()},children:(0,a.jsx)("a",{className:"link link-primary",children:"Try again"})})]});var N=(0,a.jsx)(f,{});return(0,a.jsxs)(a.Fragment,{children:[(0,a.jsx)("div",{id:"scrollableDiv",className:"cs1 ce12",onClick:r.onResultClick,children:(0,a.jsx)(l.Z,{className:"grid cs1 ce12 grid-content",scrollableTarget:"scrollableDiv",dataLength:j.length,next:y,hasMore:k,loader:(0,a.jsx)("div",{className:"grid-notice",children:N}),endMessage:(0,a.jsx)("div",{className:"grid-notice",children:w?"Your search did not match any images.":x?N:(0,a.jsxs)("div",{className:"grid-count",children:[j.length," results"]})}),children:j.map((function(r,e){var n;return(0,a.jsx)("div",{tabIndex:1,className:"grid-thumbnail",children:(0,a.jsx)(s(),{"data-type":r.type,"data-url":"image/"===r.type?r.thumbnail.url:r.url,src:null===(n=r.thumbnail)||void 0===n?void 0:n.url,alt:r.description||"",title:r.description||"",layout:"fill",objectFit:"cover",draggable:!1,className:"miro-draggable draggable-item",quality:100,unoptimized:!0})},e)}))})}),(0,a.jsxs)("div",{className:"cs1 ce12 p-small copy-notice",children:["Images might be subject to copyright. ",(0,a.jsx)("a",{rel:"noreferrer",href:"https://support.google.com/legal/answer/3463239?hl=en",target:"_blank",children:"Learn more"})]})]})}},1720:function(r,e,n){"use strict";n.r(e),n.d(e,{default:function(){return m}});var t=n(5893),i=n(9008),a=n.n(i),o=n(4298),c=n.n(o),s=n(4051),l=n.n(s),u=n(7294);n(4830);function d(r,e,n,t,i,a,o){try{var c=r[a](o),s=c.value}catch(l){return void n(l)}c.done?e(s):Promise.resolve(s).then(t,i)}function f(r){return function(){var e=this,n=arguments;return new Promise((function(t,i){var a=r.apply(e,n);function o(r){d(a,t,i,o,c,"next",r)}function c(r){d(a,t,i,o,c,"throw",r)}o(void 0)}))}}function h(){return(h=f(l().mark((function r(){return l().wrap((function(r){for(;;)switch(r.prev=r.next){case 0:console.log("Initializing Miro",miro.board),miro.board.ui.on("icon:click",f(l().mark((function r(){return l().wrap((function(r){for(;;)switch(r.prev=r.next){case 0:return r.next=2,miro.board.ui.openPanel({url:"/sidebar",height:800});case 2:case"end":return r.stop()}}),r)}))));case 2:case"end":return r.stop()}}),r)})))).apply(this,arguments)}var p=function(){return(0,u.useEffect)((function(){!function(){h.apply(this,arguments)}()})),(0,t.jsx)(t.Fragment,{children:(0,t.jsx)("div",{children:"This is just a placeholder for the app boostrapping part."})})};function m(){return(0,t.jsxs)("div",{children:[(0,t.jsxs)(a(),{children:[(0,t.jsx)("title",{children:"Miro \u2013 Google Image Search"}),(0,t.jsx)("meta",{name:"description",content:"Google Image Search"})]}),(0,t.jsx)(c(),{src:"https://miro.com/app/static/sdk/v2/miro.js",strategy:"beforeInteractive"}),(0,t.jsx)(p,{})]})}},9008:function(r,e,n){r.exports=n(3121)}},function(r){r.O(0,[678,774,888,179],(function(){return e=8312,r(r.s=e);var e}));var e=r.O();_N_E=e}]);