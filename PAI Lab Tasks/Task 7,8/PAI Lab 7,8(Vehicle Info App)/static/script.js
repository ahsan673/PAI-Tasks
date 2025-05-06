function validateForm() {
    const vin = document.getElementById("vin").value.trim();
    if (vin.length !== 17) {
        alert("VIN must be exactly 17 characters long.");
        return false;
    }
    return true;
}
