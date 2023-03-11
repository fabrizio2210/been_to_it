<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
  msg: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <div id="invito">
    <img
      width="100%"
      src="@/assets/invito_settembre_bg.jpg"
      alt="background image"
    />
    <p id="par1" style="top: 52%; left: 54%" class="ft16">
      Dalle&nbsp;11.00&nbsp;alle&nbsp;11.30<br />
      &nbsp;Palazzo&nbsp;Geremia,&nbsp;<br />
      via&nbsp;Belenzani&nbsp;20,&nbsp;Trento&nbsp;
    </p>
    <p id="par2" style="top: 66%; left: 58%" class="ft11">
      Seguirà&nbsp;un&nbsp;breve&nbsp;aperitivo&nbsp;<br />
      in&nbsp;città&nbsp;per&nbsp;poi&nbsp;spostarci&nbsp;<br />
      sul&nbsp;monte&nbsp;di&nbsp;Mezzocorona&nbsp;<br />
      alla&nbsp;baita&nbsp;del&nbsp;Ciano
    </p>
    <p id="par3" style="top: 79.5%; left: 58.5%" class="ft11">
      Per&nbsp;favore,&nbsp;conferma&nbsp;la&nbsp;tua<br />
      presenza&nbsp;tramite&nbsp;telefono<br />
      3471226481&nbsp;o&nbsp;mail<br />
      fabrizio2210@gmail.com<br />
    </p>
  </div>
</template>

<style scoped>
@font-face {
  font-family: "glacial-indifference-regular";
  src: local("glacial-indifference-regular"),
    url(@/assets/GlacialIndifference-Regular.ttf) format("truetype");
}
@font-face {
  font-family: "glacial-indifference-bold";
  src: local("glacial-indifference-regular"),
    url(@/assets/GlacialIndifference-Bold.ttf) format("truetype");
}

#invito {
  position: relative;
  width: 100%;
}
p {
  margin: 0;
  padding: 0;
  text-align: center;
  white-space: nowrap;
  position: absolute;
  line-height: 1.15;
}
.ft11 {
  font-size: 9px;
  font-family: glacial-indifference-regular;
  color: #000000;
}
.ft16 {
  font-size: 11px;
  font-family: glacial-indifference-bold;
  color: #000000;
}

@media (min-width: 380px) {
  .ft11 {
    font-size: 9.5px;
  }
  .ft16 {
    font-size: 12px;
  }
}
@media (min-width: 400px) {
  .ft11 {
    font-size: 10px;
  }
  .ft16 {
    font-size: 14px;
  }
}
@media (min-width: 500px) {
  .ft11 {
    font-size: 12px;
  }
  .ft16 {
    font-size: 16px;
  }
}
@media (min-width: 595px) {
  .ft11 {
    font-size: 15px;
  }
  .ft16 {
    font-size: 20px;
  }
}
@media (min-width: 760px) {
  .ft11 {
    font-size: 20px;
  }
  .ft16 {
    font-size: 25px;
  }
}
@media (min-width: 830px) {
  .ft11 {
    font-size: 22px;
  }
  .ft16 {
    font-size: 27px;
  }
}
@media (min-width: 915px) {
  .ft11 {
    font-size: 25px;
  }
  .ft16 {
    font-size: 30px;
  }
}
@media (min-width: 1024px) {
  #invito {
    width: 1024px;
  }
  .ft11 {
    font-size: 30px;
  }
  .ft16 {
    font-size: 34px;
  }
}
</style>
