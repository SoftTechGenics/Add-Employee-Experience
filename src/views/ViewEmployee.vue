<template>
    <div class="container mt-3">
       <div class="row">
           <div class="col">
               <p class="h3 text-black fw-bold">View Employee</p>
               <p class="fst-italic">You are viewing Employee's information.</p>
           </div>
       </div>
    </div>
    <div class="container">
        <div class="row align-items-center">
            <div class="col-md-4">
                <img src="https://www.pngitem.com/pimgs/m/0-6243_user-profile-avatar-scalable-vector-graphics-icon-woman.png" alt="" class="contact-img-big">

            </div>
            <div class="col-md-6">
                <ul class="list-group">
                            <li class="list-group-item">Name: <span class="fw-bold">Name</span></li>
                            <li class="list-group-item">Email: <span class="fw-bold">Email</span></li>
                            <li class="list-group-item">Job Title: <span class="fw-bold">Job Title</span></li>
                            <li class="list-group-item">Experience: <span class="fw-bold">Experience</span></li>
                            <li class="list-group-item">Mobile: <span class="fw-bold">Mobile</span></li>
                            <li class="list-group-item">Employee Category: <span class="fw-bold">Type</span></li>
                        </ul>

            </div>

        </div>
        <div class="row mt-3">
            <div class="col">
                <router-link to="/" class="btn btn-success"><i class="fa fa-arrow-alt-circle-left"></i> Back</router-link>
            </div>

        </div>
    </div>
</template>

<script>
export default {
    name: "ViewEmployee"
}
</script>

<style scoped>

</style>