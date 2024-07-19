module com.theharoldhotel {
    requires javafx.controls;
    requires javafx.fxml;

    opens com.theharoldhotel to javafx.fxml;
    exports com.theharoldhotel;
}
