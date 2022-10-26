<template>
 <div class="container mt-3">
    <div class="row">
        <div class="col">
            <p class="h3 text-black fw-bold">Add Employee</p>
            <p class="fst-italic">Fill the form given below to add new employee.</p>
        </div>
    </div>
 </div>
 <div class="container mt-3">
    <div class="row">
        <div class="col-md-6">
            <form>
                <div class="mb-2">
                    <input type="text" class="form-control" placeholder="Name">

                </div>
                <div class="mb-2">
                    <input type="text" class="form-control" placeholder="Photo URL">

                </div>
                <div class="mb-2">
                    <input type="Email" class="form-control" placeholder="Email">

                </div>
                <div class="mb-2">
                    <input type="number" class="form-control" placeholder="Mobile">

                </div>
                <div class="mb-2">
                    <input type="text" class="form-control" placeholder="Job Title">

                </div>
                <div class="mb-2">
                    <input type="text" class="form-control" placeholder="Experience">

                </div>
                <div class="mb-2">
                    <select class="form-control">
                        <option value="">Select Employee Category</option>"
                    </select>
                </div>
                <div class="mb-2">
                    <input type="submit" class="btn btn-success" value="Create">

                </div>
            
            </form>
        </div>
        <div class="col-md-4">
            <img src="https://www.pngitem.com/pimgs/m/0-6243_user-profile-avatar-scalable-vector-graphics-icon-woman.png" alt="" class="contact-img">
    </div>
</div>
 </div>
</template>

<script>
export default {
    name: "AddEmployee"
}
</script>

<style scoped>

</style>