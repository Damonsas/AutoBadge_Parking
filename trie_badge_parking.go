package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	// "github.com/xuri/excelize/v2"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run trie_badge_parking.go <badge_number>")
		return
	}

	badgeNumber, err := strconv.Atoi(os.Args[1])
	if err != nil {
		log.Fatalf("Erreur : l'argument doit être un entier. %v", err)
	}

	filepath := "C:/Users/danhk/OneDrive/Bureau/Liste_Abonnés.xlsx"
	f, err := excelize.OpenFile(filepath)
	if err != nil {
		log.Fatalf("Erreur lors de la lecture de donnée: %v", err)
	}

	rows, err := f.GetRows(f.GetSheetName(0))
	if err != nil {
		log.Fatalf("Erreur lors de la lecture de donnée: %v", err)
	}

	found := false
	for _, row := range rows {
		if len(row) > 0 {
			id, err := strconv.Atoi(row[0])
			if err == nil && id == badgeNumber {
				fmt.Printf("Badge trouvé : %s, %s, %s, %v\n", row[0], row[3], row[5])
				found = true
				break
			}
		}

	}

	if !found {
		fmt.Println("Badge non trouvé.")
	}
}
