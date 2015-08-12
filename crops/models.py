from django.db import models


class Category(models.Model):
    SUMMER = 'summer'
    WINTER = 'winter'
    SPRING = 'spring'
    FALL = 'fall'
    SEASON_OPTIONS = (
        (SUMMER, 'Summer'),
        (WINTER, 'Winter'),
        (SPRING, 'Spring'),
        (FALL, 'Fall'),
    )
    name = models.CharField(max_length=255, choices=SEASON_OPTIONS,
        default=WINTER)

    def __str__(self):
        return "{0}".format(self.name).capitalize()

    class Meta:
        verbose_name_plural = 'categories'


class Crop(models.Model):
    TIER_ONE = '1'
    TIER_TWO = '2'
    TIER_THREE = '3'
    TIER_OPTIONS = (
        (TIER_ONE, 'Tier 1'),
        (TIER_TWO, 'Tier 2'),
        (TIER_THREE, 'Tier 3'),
    )
    name = models.CharField(max_length=255)
    plant_start_date = models.DateField(auto_now=False)
    plant_end_date = models.DateField(auto_now=False)
    tier = models.CharField(max_length=255, choices=TIER_OPTIONS,
        default=TIER_ONE)
    transplant = models.BooleanField(default=None)
    direct_seed = models.BooleanField(default=None)
    category = models.ForeignKey(Category, related_name="crops")
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
