
## Reads the high score files
def read_high_scores(index):
    high_scores = []
    with open(f'highscores/highscore{index}.txt', 'r') as file:
        for line in file:
            score = int(line.strip())
            high_scores.append(score)
    return high_scores

## Updates the high score files
def update_high_scores(new_score,index):
    high_scores = read_high_scores(index)
    if len(high_scores) < 5 or new_score>min(high_scores) :
        high_scores.append(new_score)
        high_scores.sort(reverse=True)
        high_scores = high_scores[:5]  # Keep only the top 5 scores
        with open(f'highscores/highscore{index}.txt', 'w') as file:
            file.truncate(0)
            for score in high_scores:
                file.write(str(score) + '\n')
                