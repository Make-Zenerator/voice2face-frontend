<script>
  export let property1 = "github";
  let className = "";
  export { className as class };
  export let style;
  const variantsClassName = "property-1-" + property1;
  export let targetPath = "";

  function navigate() {
    window.location.href = targetPath;
  }
</script>

<style>
  .social-property-1-github {
    flex-shrink: 0;
    width: 30px;
    height: 30px;
    position: relative;
    overflow: visible;
    cursor: pointer;
  }
</style>

<img
  class="social-property-1-github {className} {variantsClassName}"
  style={style}
  src="logo/github.png"
  on:click={navigate}
/>
