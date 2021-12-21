<script context="module">
    export const load = async({page, fetch}) => {
        const id = page.params.id;       
        const res = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
        const post = await res.json();

        return {
            props: {
                post,
            },
        };
    };
</script>

<div class="post">
    <h2>{post.title}</h2>
    <p>{post.body}</p>
</div>

<script>
    export let post;
</script>