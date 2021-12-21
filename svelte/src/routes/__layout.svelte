<script>

import { append_styles } from "svelte/internal";

</script>
<div class="container">
    <slot />
</div>

<style>
    .container {
        max-width: 600px;
        margin: 50px auto;
    }
</style>