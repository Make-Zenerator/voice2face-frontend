<script>
	import {Router, Link, Route} from "svelte-routing"
	import Join from "./routes/join.svelte"
	import Login from "./routes/login.svelte"
	import Main from "./routes/main.svelte"

	export let url = "";
</script>
<Router {url}>
	<nav>
		<Link to="/" component= {Main} />
		<Link to="/join" component={Join}/>
		<Link to="/login" component={Login}/>
	</nav>
	<div>
		<Route path="/" component={Main}/>
		<Route path="/join" component={Join} />
		<Route path="/login" component={Login} />
	</div>
</Router>