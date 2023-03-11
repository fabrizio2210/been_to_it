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
  <div id="page1-div" style="position: relative; width: 1080px; height: 1511px">
    <img
      width="1080"
      height="1511"
      src="@/assets/invito_bg.jpg"
      alt="background image"
    />
    <p style="position: absolute; top: 1212px; left: 628px" class="ft11">
      Per&nbsp;favore,&nbsp;conferma&nbsp;la&nbsp;tua<br />
      presenza&nbsp;tramite&nbsp;telefono<br />
      3471226481&nbsp;o&nbsp;mail<br />
      fabrizio2210@gmail.com<br />
    </p>
    <p style="position: absolute; top: 1002px; left: 624px" class="ft11">
      Seguirà&nbsp;un&nbsp;breve&nbsp;aperitivo&nbsp;<br />
      in&nbsp;città&nbsp;per&nbsp;poi&nbsp;spostarci&nbsp;<br />
      sul&nbsp;monte&nbsp;di&nbsp;Mezzocorona&nbsp;<br />
      alla&nbsp;baita&nbsp;del&nbsp;Ciano
    </p>
    <p style="position: absolute; top: 814px; left: 587px" class="ft16">
      <b
        >Dalle&nbsp;11.00&nbsp;alle&nbsp;11.30<br />
        &nbsp;Palazzo&nbsp;Geremia,&nbsp;<br />
        via&nbsp;Belenzani&nbsp;20,&nbsp;Trento&nbsp;</b
      >
    </p>
  </div>
</template>

<style scoped>
p {
  margin: 0; padding: 0; text-align: center; white-space:nowrap
}
.ft11 {
  font-size:30px;font-family:BAAAAA+GlacialIndifference;color:#000000;
}
.ft16 {
  font-size:34px;font-family:AAAAAA+GlacialIndifference;color:#000000;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
