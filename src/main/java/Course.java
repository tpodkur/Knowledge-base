
public class Course {
    private String title;
    private String description;
    private Integer cost;
    private String section;

    public Course(String title, String description, Integer cost, String section) {
        this.title = title;
        this.description = description;
        this.cost = cost;
        this.section = section;
    }

    public String getTitle() { return title; }
    public String getDescription() { return description; }
    public Integer getCost() { return cost; }
    public String getSection() { return section; }
}
