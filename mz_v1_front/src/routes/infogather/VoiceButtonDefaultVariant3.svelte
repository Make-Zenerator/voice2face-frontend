<script>
  export let variant = 'variant-3';
  let className = '';
  export { className as class }; export let style;const variantsClassName = 'default-' + variant
</script>
<div style="{'width: 50px; height: 50px; position: relative; ' + style}">
  <img
    class="{'frame-6 ' + className + ' ' + variantsClassName}"
    style="
      display: flex;
      flex-direction: row;
      gap: 10px;
      align-items: flex-start;
      justify-content: flex-start;
      height: auto;
      position: absolute;
      left: calc(50% - 25px);
      bottom: 0%;
      top: 0%;
      height: 100%;
      overflow: visible;
    "
    src="/join/frame-60.svg"
  />
</div>
