import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class hello extends Application {

    @Override
    public void start(Stage primaryStage) {
        // Set the Atlantafx CSS theme
        Application.setUserAgentStylesheet(getClass().getResource("/css/atlantafx-base.css").toExternalForm());

        Button button = new Button("Hello Atlantafx");

        StackPane root = new StackPane(button);
        Scene scene = new Scene(root, 400, 300);

        primaryStage.setTitle("Hello Atlantafx");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}