<template>
   <div class="container mt-3">
    <div class="row">
        <div class="col">
        <p class="h3 text-black fw-bold">Employees Manager 
            <router-link to="/employees/add" class="btn btn-black btn-sm"><i class="fa fa-plus-circle"></i>New</router-link>
        </p>
        <p class="fst-italic">Welcome to the employees IUB website! Where you can manage your employees through this WebApp.</p>
        <form>
            <div class="row">
                <div class="col-md-6">
                    <div class="row">
                        <div class="col">
                    <input type="text" class="form-control" placeholder="Search Name">
                </div>
                <div class="col">
                    <input type="submit" class="btn btn-outline-dark">
                </div>
                    </div>
                </div>
            </div>
        </form>
     </div>
    </div>
   </div>
   <div class="container mt-3">
    <div class="row">
        <div class="col-md-6">
            <div class="card my-2 list-group-item-success shadow-lg">
                <div class="card-body">
                    <div class="row align-items-center">
                      <div class="col-sm-4">
             <img src="https://www.pngitem.com/pimgs/m/0-6243_user-profile-avatar-scalable-vector-graphics-icon-woman.png" alt="" class="contact-img">
                      </div>
                      <div class="col-sm-7">
                        <ul class="list-group">
                            <li class="list-group-item">Name: <span class="fw-bold">Name</span></li>
                            <li class="list-group-item">Email: <span class="fw-bold">Email</span></li>
                            <li class="list-group-item">Job Title: <span class="fw-bold">Job Title</span></li>
                        </ul>

                      </div>
                      <div class="col-sm-1 d-flex flex-column justify-content-center align-items-center">
                        <router-link to="employees/view/:employeeId" class="btn btn-warning my-1">
                            <i class="fa fa-eye"></i>
                        </router-link>
                        <router-link to="employees/edit/:employeeId" class="btn btn-primary my-1">
                            <i class="fa fa-pen"></i>
                        </router-link>
                        <button class="btn btn-danger my-1">
                            <i class="fa fa-trash"></i>
                        </button>

                      </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
   </div>
</template>

<script>
export default {
    name: "EmployeesManager"
}
</script>

<style scoped>

</style>