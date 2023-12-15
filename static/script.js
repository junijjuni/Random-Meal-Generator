$(document).ready(function () {
    // Hide the meal information initially
    $("#meal-info").hide();

    $("#generate-btn").click(function () {
        const dietOption = $("#diet_option").val();
        const cuisineType = $("#cuisine_type").val();

        $.post("/get_random_meal", { diet_option: dietOption, cuisine_type: cuisineType }, function (data) {
            if (data.error) {
                alert(data.error);
            } else {
                // Display the meal information
                $("#meal-name").text(data.name);
                $("#meal-image").attr("src", data.image);
                const ingredientsList = $("#ingredients-list");
                ingredientsList.empty();
                data.ingredients.forEach(function (ingredient) {
                    ingredientsList.append("<li>" + ingredient + "</li>");
                });

                // Clear the selection form inputs
                $("#diet_option").val('');
                $("#cuisine_type").val('');

                // Show the meal information and keep the selection form visible
                $("#meal-info").show();
            }
        });
    });
});