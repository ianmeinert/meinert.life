<script context="module">
    export const load = async({fetch}) => {
        const res = await fetch("https://jsonplaceholder.typicode.com/posts");

        const posts = await res.json();

        return {
            props: {
                posts,
            },
        };
    };
</script>

<script>
    import { paginate, LightPaginationNav } from 'svelte-paginate'

    export let posts;
     
    let items = posts.reverse();
    let currentPage = 1;
    let pageSize = 4;
    
    $: paginatedPosts = paginate({ items, pageSize, currentPage });
</script>
<h1>Ramblings</h1>

<div class="posts">
    {#each paginatedPosts as post}
        <div class="post">
            <h2>{post.title.substring(0, 20)}</h2>
            <p>{post.body.substring(0, 80)}</p>
            <p class="readmore"><a href={`/blog/${post.id}`}>Read More</a></p>
        </div>
    {/each}
</div>

<LightPaginationNav
    totalItems="{items.length}"
    pageSize="{pageSize}"
    currentPage="{currentPage}"
    limit="{1}"
    showStepOptions="{true}"
    on:setPage="{(e) => currentPage = e.detail.page}"
/>

<style>
    .posts {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-gap: 20px;
    }

    .post {
        padding: 10px;
        border: 1px solid #ddd;
        box-shadow: 0 0 10px #eee;
    }

    h2 {
        margin: 0;
    }

    .readmore {
        text-align: right;
    }
</style>